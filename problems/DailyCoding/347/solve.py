from typing import Optional, Set


def solve(string: str, k: int) -> str:
	seen: Set[str] = set()
	best = string

	chars = list(string)
	while True:
		string = ''.join(chars)
		if string in seen:
			break
		seen.add(string)
		best = min(best, string)

		found: Optional[str] = None
		for i, blocker in enumerate(chars[:k]):
			for blocking in chars[i + 1:k]:
				if blocker > blocking:
					found = blocker
					break
			else:
				continue
			break
		found = found or sorted(chars[:k])[0]

		i = chars.index(found)
		del chars[i]
		chars.append(found)

	return best


def test_solve():
	for i in range(1, 5):
		assert solve('daily', i) == 'ailyd'
	assert solve('daily', 5) == 'adily'
