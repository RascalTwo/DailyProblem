from typing import List, Optional



def solve(words: List[str]) -> Optional[List[str]]:
	return (
		words
		if len(words) == 1 else
		next((
			[words[0]] + circle
			for i, word in enumerate(words[1:])
			if words[0].endswith(word[0]) and
			(circle := solve(
				[word] + [
					loop_word
					for li, loop_word in enumerate(words[1:])
					if li != i
				])
			)
		), None)
	)


def test_solve():
	assert solve(['cat', 'taco']) == ['cat', 'taco']
	assert solve(['taco', 'cat']) == None
	assert solve(['cat', 'opera', 'taco']) == ['cat', 'taco', 'opera']
	assert solve(['cat', 'omega', 'taco', 'alpha']) == ['cat', 'taco', 'omega', 'alpha']
	assert solve(['chair', 'height', 'racket', 'tunic', 'touch']) == ['chair', 'racket', 'touch', 'height', 'tunic']
	assert solve(['chair', 'height', 'racket', 'tunic', 'touchy']) is None
