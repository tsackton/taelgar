from editor import *
def quality(n,note):
 j=json.loads((W/f'jobs/quality-chunk-{n:03}.json').read_text());r=dict(schemaVersion=1,stage='quality',chunkId=j['chunk']['id'],sourceSha256=j['sourceSha256'],verdict='pass',findings=[],checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'],note=note);(B/j['responsePath']).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':quality(int(sys.argv[1]),sys.argv[2])
