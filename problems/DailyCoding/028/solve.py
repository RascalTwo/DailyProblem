from typing import List



def justify_words(words: List[str], width: int) -> str:
	extra_spaces = width - len(' '.join(words))
	if len(words) == 1:
		return ' ' * extra_spaces + words[0]

	i = 0
	for _ in range(extra_spaces):
		words[i] += ' '
		i = (i + 1) % (len(words) - 1)
	return ' '.join(words)


def solve(words: List[str], width: int) -> List[str]:
	lines: List[str] = []
	line: List[str] = []
	while words:
		line.append(words.pop(0))
		length = len(' '.join(line))
		if length <= width:
			continue
		words.insert(0, line.pop(-1))
		lines.append(justify_words(line, width))
		line = []

	if line:
		lines.append(justify_words(line, width))


	return lines


def test_solve():
	'''assert solve(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16) == [
		"the  quick brown",
		"fox  jumps  over",
		"the   lazy   dog"
	]'''
	assert solve(['hello', 'world,', 'how', 'are', 'you', 'this', 'lovely', 'day?'], 15) == [
		'hello    world,',
		'how   are   you',
		'this     lovely',
		'           day?'
	]
