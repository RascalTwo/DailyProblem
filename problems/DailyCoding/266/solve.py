import string



from typing import Iterable, List



def solve(dictionary: List[str], word: str) -> Iterable[str]:
	characters: List[str] = [''.join(sorted(possible)) for possible in dictionary]

	sorted_word = ''.join(sorted(word))
	for char in string.ascii_uppercase:
		chars = ''.join(sorted(sorted_word + char))
		index = 0
		while True:
			try:
				index = characters.index(chars, index)
				yield dictionary[index]
				index += 1
			except ValueError:
				break


def test_solve():
	assert list(solve(['APPEAL', 'DAPPLE', 'LAPPED', 'DUMMY'], 'APPLE')) == ['APPEAL', 'DAPPLE', 'LAPPED']
