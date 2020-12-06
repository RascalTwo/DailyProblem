import random
import string


from typing import Optional



class Shortener:
	pool = string.ascii_letters + string.digits


	def __init__(self):
		self.urls = []
		self.shorts = []


	@staticmethod
	def _generate_short() -> str:
		return ''.join(random.choice(Shortener.pool) for _ in range(6))


	def shorten(self, url: str) -> str:
		try:
			return self.shorts[self.urls.index(url)]
		except:
			pass

		self.urls.append(url)

		short = self._generate_short()
		self.shorts.append(short)
		return short


	def restore(self, short: str) -> Optional[str]:
		try:
			return self.urls[self.shorts.index(short)]
		except:
			return None


def test_solve():
	shortener = Shortener()

	for url, shortened in [(url, shortener.shorten(url)) for url in ('abc', 'def', 'ghi')]:
		assert shortener.restore(shortened) == url
		assert shortener.shorten(url) == shortened
