from typing import Iterable, List, Tuple



def next_term(term: str) -> str:
	counts: List[Tuple[int, str]] = []
	index = 0
	count = 1
	for i in range(1, len(term)):
		if term[i] == term[index]:
			count += 1
		else:
			counts.append((count, term[index]))
			index = i
			count = 1
	if count:
		counts.append((count, term[index]))

	term = ''
	for count, char in counts[::-1]:
		term = str(count) + char + term
	return term


def next_terms(term: str, n: int) -> Iterable[str]:
	for _ in range(n):
		term = next_term(term)
		yield term


def test_solve():
	assert next_term('1223334444') == '11223344'
	assert list(next_terms('2', 7)) == ['12', '1112', '3112', '132112', '1113122112', '311311222112', '13211321322112']