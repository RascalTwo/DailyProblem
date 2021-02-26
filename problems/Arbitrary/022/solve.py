def defang(uri: str) -> str:
	return uri.replace('.', '[.]')


def refang(uri: str) -> str:
	return uri.replace('[.]', '.')


def test_solve():
	assert defang('192.168.1.1') == '192[.]168[.]1[.]1'
	assert refang('192[.]168[.]1[.]1') == '192.168.1.1'

	assert defang('http://www.google.com/') == 'http://www[.]google[.]com/'
	assert refang('http://www[.]google[.]com/') == 'http://www.google.com/'
