import codecs



def solve(hex: str) -> str:
	return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode().strip()


def test_solve():
	assert solve('deadbeef') == '3q2+7w=='
