from typing import Dict, Set


class Soundex:
	def __init__(self, similar_consonants: Dict[str, str], vowels: Set[str], consonant_digits: Dict[int, Set[str]]):
		self.similar_consonants = similar_consonants
		self.vowels = vowels
		self.consonant_digits = consonant_digits

	def categorize(self, word: str) -> str:
		first = word[0]
		for source, dest in self.similar_consonants.items():
			word = word.replace(source, dest)

		word = word[1:]

		for vowel in self.vowels:
			word = word.replace(vowel, '')

		for digit, replacing in self.consonant_digits.items():
			str_digit = str(digit)
			for char in replacing:
				word = word.replace(char, str_digit)

		word = ''.join(char for i, char in enumerate(word[:-1]) if word[i + 1] != char) + word[-1]

		while len([char for char in word if char.isnumeric()]) != 3:
			word += '0'

		return first + word


def test_solve():
	soundex = Soundex(
		{'ck': 'c'},
		{'a', 'e', 'i', 'o', 'u', 'y', 'w', 'h'},
		{
			1: {'b', 'f', 'p', 'v'},
			2: {'c', 'g', 'j', 'k', 'q', 's', 'x', 'z'},
			3: {'d', 't'},
			4: {'l'},
			5: {'m', 'n'},
			6: {'r'},
		}
	)
	assert soundex.categorize('Jackson') == 'J250'
	assert soundex.categorize('Jaxen') == 'J250'
