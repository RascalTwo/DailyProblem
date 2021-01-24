def solve(a: str, b: str) -> bool:
	return (
		all([a, b])
		and
		len(a) == len(b)
		and
		any(a[i:] + a[0:i] == b for i in range(len(a)))
	)


def test_solve():
	assert solve('abcde', 'cdeab') is True
	assert solve('abc', 'acb') is False

	assert solve('abcd', 'abcd') is True
	assert solve('abcd', 'dabc') is True
	assert solve('abcd', 'cdab') is True
	assert solve('abcd', 'bcda') is True
