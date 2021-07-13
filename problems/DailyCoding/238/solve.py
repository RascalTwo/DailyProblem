import random

from typing import Callable, Dict, List, Literal, Union

Action = Union[Literal['hit'], Literal['pass']]
Winner = Union[Literal['draw'], Literal['player'], Literal['dealer']]



class Game:
	def __init__(self):
		self.deck: List[int] = []
		for _ in range(4):
			self.deck.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
		random.shuffle(self.deck)

		self.player: List[int] = [self.deck.pop(), self.deck.pop()]
		self.dealer: List[int] = [self.deck.pop(), self.deck.pop()]

	def calculate_winner(self):
		p_score = sum(self.player)
		if p_score > 21:
			p_score = 0

		d_score = sum(self.dealer)
		if d_score > 21:
			d_score = 0

		if p_score == d_score:
			return 'draw'
		return 'player' if p_score > d_score else 'dealer'


	def move(self, action: Action):
		if action == 'hit':
			self.player.append(self.deck.pop())
			if sum(self.player) > 21:
				return self.calculate_winner()
		else:
			if sum(self.dealer) >= 16:
				return self.calculate_winner()
			self.dealer.append(self.deck.pop())


def solve(game: Game) -> Callable[[], Action]:
	def get_move():
		if sum(game.player) + game.deck[-1] > 21:
			return 'pass'
		else:
			return 'hit'
	return get_move


def test_solve():
	results: Dict[Winner, int] = {'player': 0, 'draw': 0, 'dealer': 0}
	for _ in range(1000):
		game = Game()
		get_move = solve(game)

		winner = None
		while not winner:
			winner = game.move(get_move())
		results[winner] += 1

	assert results['player'] > results['dealer']
