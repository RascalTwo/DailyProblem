def solve(first: str, second: str) -> int:
	if first == second:
		return 0

	if (first_empty := not first) or not second:
		return len(second if first_empty else first)

	if first[0] == second[0]:
		return solve(first[1:], second[1:])

	return 1 + min(
		solve(first, second[1:]),
		solve(first[1:], second),
		solve(first[1:], second[1:])
	)



def test_solve():
	assert solve('abc', 'bc') == 1
	assert solve('kitten', 'sitting') == 3
	assert solve('universe', 'universal') == 2
	assert solve('abc', 'def') == 3
	assert solve('', 'def') == 3
	assert solve('abc', 'cba') == 2
	assert solve('abc', 'abc') == 0
