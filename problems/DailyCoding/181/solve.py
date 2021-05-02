from typing import List



def is_palindrome(string: str) -> bool:
	return string == string[::-1]

def solve(string: str) -> List[str]:
	length = len(string)

	palindromes: List[str] = []

	left, right = 0, length
	while left < length:
		considering = string[left:left + right]
		if not is_palindrome(considering):
			right -= 1
		else:
			palindromes.append(considering)
			left += right
			right = length - left

	return palindromes


def test_solve():
	assert solve('racecarannakayak') == ['racecar', 'anna', 'kayak']
	assert solve('abc') == ['a', 'b', 'c']

