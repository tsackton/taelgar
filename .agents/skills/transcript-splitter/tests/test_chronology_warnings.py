import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from manage_beats import SourceLine, finalize_beats, validate_beats


class ChronologyWarningTest(unittest.TestCase):
    def test_discrepancies_reach_annotation_but_coverage_stays_strict(self):
        rows = [SourceLine("u0001", "First"), SourceLine("u0002", "Second")]
        beats = [dict(beatId="b1", title="First", startUid="u0001", endUid="u0001", dateStart="1749-09-16", dateEnd="1749-09-15", timeWindow=None, containsCombat=False, dateResolution="inferred", boundaryReason="Start", dateEvidence=["u0001"]),
                 dict(beatId="b2", title="Second", startUid="u0002", endUid="u0002", dateStart="1749-09-18", dateEnd=None, timeWindow=None, containsCombat=False, dateResolution="inferred", boundaryReason="Shift", dateEvidence=["u0002"])]
        beats = finalize_beats(beats, rows)
        errors, warnings = validate_beats(beats=beats, transcript_lines=rows, session_payload={"drStart": "1749-09-16"})
        self.assertEqual(errors, [])
        self.assertEqual(sum("CHRONOLOGY:" in warning for warning in warnings), 2)
        beats[1]["startUid"] = "u0001"
        errors, _ = validate_beats(beats=beats, transcript_lines=rows, session_payload={})
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
