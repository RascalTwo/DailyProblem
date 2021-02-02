class Singleton:
	__instances = (None, None)
	__call = 1


	def __new__(cls):
		if all(getattr(cls, f'_{cls.__name__}__instances')):
			return cls.getInstance()
		instance = super(Singleton, cls).__new__(cls)
		if not instance.__instances[0]:
			instance.__instances = (instance, None)
		elif not instance.__instances[1]:
			instance.__instances = (instance.__instances[0], instance)
		setattr(cls, f'_{cls.__name__}__instances', instance.__instances)
		return instance


	@staticmethod
	def getInstance():
		Singleton.__call = (Singleton.__call + 1) % len(Singleton.__instances)
		return Singleton.__instances[Singleton.__call]


def test_solve():
	first = Singleton()
	second = Singleton()
	assert Singleton() == first
	assert Singleton() == second
	assert first.getInstance() == first
	assert first.getInstance() == second
	assert second.getInstance() == first
	assert second.getInstance() == second
