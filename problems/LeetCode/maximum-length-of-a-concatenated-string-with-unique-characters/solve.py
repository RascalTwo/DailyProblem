from typing import Dict, List, Set, FrozenSet



def recur(strings: Set[FrozenSet[str]], current: FrozenSet[str], cache: Dict[FrozenSet[str], int]) -> int:
	if (cached := cache.get(current, None)) is not None:
		return cached

	best = max((
		recur(strings.copy().difference(string), current | string, cache)
		for string in strings
		if not (current & string)
	), default=len(current))
	cache[current] = best
	return best

def solve_recur(strings: List[str]) -> int:
	res: Set[FrozenSet[str]] = set()
	for string in strings:
		set_str = frozenset(string)
		if len(set_str) != len(string):
			continue
		res.add(set_str)
	return recur(res, frozenset(), {})


def solve_iter(strings: List[str]) -> int:
	seen: Set[FrozenSet[str]] = set((frozenset(), ))
	for string in strings:
		str_set = frozenset(string)
		if len(str_set) == len(string):
			seen |= set(str_set | combo for combo in seen if not (str_set & combo))
	return max((len(combo) for combo in seen), default=0)


def test_solve():
	for solve in (solve_iter, solve_recur):
		assert solve(['un', 'iq', 'ue']) == 4
		assert solve(['cha', 'r', 'act', 'ers']) == 6
		assert solve(['abcdefghijklmnopqrstuvwxyz']) == 26
		assert solve(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']) == 16
