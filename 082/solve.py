import io

def read7(file: io.TextIOWrapper) -> str:
	return file.read(7)


def readN(n: int, file: io.TextIOWrapper):
	characters = ''

	total_consumed = 0
	while total_consumed < n:
		started = file.tell()
		characters += read7(file)
		ended = file.tell()

		if started == ended:
			break

		total_consumed += ended - started


	if (over_read := total_consumed - n):
		file.seek(file.tell() - over_read)
		characters = characters[:n]

	return characters


def test_solve():
	file = io.StringIO('Hello world')
	assert [read7(file) for _ in range(3)] == ['Hello w', 'orld', '']

	file = io.StringIO('Hello world')
	assert [readN(1, file) for _ in range(3)] == ['H', 'e', 'l']

	file = io.StringIO('Hello world')
	assert [readN(5, file) for _ in range(3)] == ['Hello', ' worl', 'd']

	file = io.StringIO('Hello world')
	assert [readN(10, file) for _ in range(3)] == ['Hello worl', 'd', '']
