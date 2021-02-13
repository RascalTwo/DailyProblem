from typing import Optional, Union



def solve(string: str) -> Optional[Union[int, float]]:
	try:
		a = float(string)
		try:
			b = int(string)
			if a == b:
				return b
		except:
			return a
	except:
		if string.count('e') != 1:
			return None

		values = list(solve(part) for part in string.split('e'))
		if any(value is None for value in values):
			return None
		return pow(*values)


def test_solve():
	assert solve('10') == 10
	assert solve('-10') == -10
	assert solve('10.1') == 10.1
	assert solve('-10.1') == -10.1
	assert solve('1e5') == 100000
	assert solve('a') is None
	assert solve('x 1') is None
	assert solve('a -2') is None
	assert solve('-') is None
