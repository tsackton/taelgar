"""Common map field validation and JSON/digest representation."""
import json
from .storage import sha

CONFIDENCE_RATINGS = {'high', 'medium', 'low'}
REVIEW_STATUSES = {'unreviewed', 'automatedReviewed', 'humanReviewed'}


class MapError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise MapError(message)


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def digest(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                               separators=(',', ':'), default=str))


def object_fields(value, required, optional, label):
    require(isinstance(value, dict), f'{label} must be an object')
    require(required <= value.keys(), f'{label} missing fields: {sorted(required - value.keys())}')
    require(value.keys() <= required | optional,
            f'{label} has unknown fields: {sorted(value.keys() - required - optional)}')


def string(value, label, limit=None, nullable=False):
    if value is None and nullable:
        return
    require(isinstance(value, str) and value.strip() and '\n' not in value and '\r' not in value,
            f'{label} must be nonempty single-line text')
    if limit:
        require(len(value.split()) <= limit, f'{label} exceeds {limit} words')


def validate_review(value, label='review'):
    object_fields(value, {'confidence', 'status'}, set(), label)
    require(isinstance(value['confidence'], str) and value['confidence'] in CONFIDENCE_RATINGS,
            f'{label} has unknown confidence')
    require(isinstance(value['status'], str) and value['status'] in REVIEW_STATUSES,
            f'{label} has unknown review status')


def cell(value):
    return str(value or '—').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '\\|').replace('\n', ' ')
