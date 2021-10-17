K = 50

class Player:
	def __init__(self, name: str, score: int = 1500):
		self.name = name
		self.score = score


def reward(loser: Player, winner: Player):
	expected_loser, expected_winner = sorted([winner, loser], key=lambda x: x.score)
	wagered = int((K * expected_loser.score / expected_winner.score) // (2 if winner == expected_winner else 0.5))

	loser.score -= wagered
	winner.score += wagered


def test_solve():
	john = Player('John')
	jane = Player('Jane')

	reward(jane, john)
	assert john.score == 1600
	assert jane.score == 1400

	reward(jane, john)
	assert john.score == 1621
	assert jane.score == 1379

	jane.score = 1100
	reward(jane, john)
	assert john.score == 1637
	assert jane.score == 1084

	reward(john, jane)
	assert john.score == 1571
	assert jane.score == 1150
