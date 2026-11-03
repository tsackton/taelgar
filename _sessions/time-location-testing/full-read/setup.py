"""Bind existing pilot helpers to this separate two-session experiment."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent))
import read_source,authoring
read_source.SAMPLE=json.loads((ROOT/'sample.json').read_text())
authoring.ROOT=ROOT
Study=authoring.Study
load=read_source.load
PAT=read_source.PAT
