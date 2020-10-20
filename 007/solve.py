MAPPING = {str(i): chr(96 + i) for i in range(1, 27)}


def get_possible_decodings(encoded: str):
	decodings = set()

	for i in range(len(encoded)):
		considering = encoded[i:]
		for char, suffix in ((char, encoded[len(num):]) for num, char in MAPPING.items() if considering.startswith(num)):
			decodings |= set(char + possible for possible in get_possible_decodings(suffix)) if suffix else set(char)

	return decodings


def test_solve():
	assert len(get_possible_decodings('1')) == 1
	assert len(get_possible_decodings('12')) == 3
	assert len(get_possible_decodings('111')) == 3
	assert len(get_possible_decodings('1111')) == 5
	assert len(get_possible_decodings('121')) == 8
