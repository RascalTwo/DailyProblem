from typing import List, Optional



def solve(words: str, a: str, b: str) -> Optional[int]:
	word_list = words.split(' ')
	firsts: List[int] = []
	seconds: List[int] = []
	best = None
	for i, word in enumerate(word_list):
		if word == a:
			firsts.append(i)
		if word == b:
			seconds.append(i)

	best: Optional[int] = None
	for f in firsts:
		for s in seconds:
			dist = abs(f - s) - 1
			if best is None or dist < best:
				best = dist
	return best

def test_solve():
	assert solve('dog cat hello cat dog dog hello cat world', 'hello', 'world') == 1
	assert solve('abc zzz zzz zzz def zzz abc zzz def abc', 'abc', 'def') == 0
	assert solve('a b c', 'c', 'd') == None
