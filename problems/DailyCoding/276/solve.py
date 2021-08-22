from typing import Optional



def solve(string: str, substring: str) -> Optional[int]:
	return next((i for i in range(len(string) - len(substring) + 1) if string[i:i + len(substring)] == substring), False)


def test_solve():
	assert solve('supercalifragilisticexpialidocious', 'super') == 0
	assert solve('supercalifragilisticexpialidocious', 'docious') == 27
	assert solve('supercalifragilisticexpialidocious', 'fragil') == 9
	assert solve('supercalifragilisticexpialidocious', 'nonezo') is False
