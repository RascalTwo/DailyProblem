from typing import Iterable



def solve(string: str, *words: str) -> Iterable[int]:
	word_length = len(words[0])
	total_words_length = sum(map(len, words))

	for s in range(len(string) - total_words_length + 1):
		attempt = list(words)
		while attempt:
			word = string[s:s + word_length]
			if word not in attempt:
				break
			attempt.remove(word)
			s += word_length

		if not attempt:
			yield s - total_words_length


def test_solve():
	assert list(solve('barfoothefoobarman', 'foo', 'bar')) == [0, 9]
	assert list(solve('wordgoodgoodgoodbestword', 'word', 'good', 'best', 'word')) == []
	assert list(solve('barfoofoobarthefoobarman', 'bar', 'foo', 'the')) == [6, 9, 12]
	assert list(solve('wordgoodgoodgoodbestword', 'word', 'good', 'best', 'good')) == [8]
