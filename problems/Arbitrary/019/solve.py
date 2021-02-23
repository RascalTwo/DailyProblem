def solve(a: str, b: str) -> bool:
	if a == b:
		return True

	if len(b) > len(a):
		a, b, = b, a

	a = ' ' + a
	b = ' ' + b
	while True:
		a = a[1:]
		b = b[1:]
		if a == b:
			return True

		if not b:
			return len(a) == 1

		if a[0] == b[0]:
			continue

		if a[1:] == b[1:]:
			return True
		if a[1:] == b:
			return True
		if a == b[1:]:
			return True

		return False


def test_solve():
	assert solve('pale', 'ple') is True
	assert solve('pales', 'pale') is True
	assert solve('pale', 'bale') is True
	assert solve('pale', 'bae') is False
	assert solve('abcd', 'dcba') is False
	assert solve('1234', '1234') is True
	assert solve('1234', '12345') is True
	assert solve('1234', '123456') is False
	assert solve('1234', '123') is True
	assert solve('1234', '12') is False
