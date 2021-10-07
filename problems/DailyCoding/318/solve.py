def solve(required: int, songs: int, buffer: int) -> int:
	return 0 if buffer > songs else 1 if not required else songs * solve(
		required - 1,
		songs - bool(buffer),
		max(0, buffer - 1)
	)


def test_solve():
	assert solve(4, 1, 1) == 0
	assert solve(4, 1, 0) == 1
	assert solve(4, 2, 1) == 2
	assert solve(4, 2, 0) == 16
	assert solve(6, 2, 0) == 64
	assert solve(9, 2, 0) == 512
	assert solve(9, 3, 0) == 19683
	assert solve(9, 3, 1) == 768
	assert solve(9, 3, 2) == 6
