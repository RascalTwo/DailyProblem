import itertools


def throw_dice(n: int, faces: int, total: int) -> int:
	return len({
		combo
		for combo in itertools.combinations((
			face
			for dice_faces in (
				list(range(1, faces + 1))
				for _ in range(n)
			)
			for face in dice_faces
		), 3)
		if sum(combo) == total
	})


def test_throw_dice():
	assert throw_dice(3, 6, 7) == 15
