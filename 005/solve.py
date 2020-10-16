from typing import Any, Callable



InnerPair = Callable[[Any, Any], Any]
Pair = Callable[[InnerPair], Any]


def car(pair: Pair):
	return pair(lambda a, _: a)


def cdr(pair: Pair):
	return pair(lambda _, b: b)


def cons(a: Any, b: Any) -> Pair:
  def pair(f: InnerPair):
    return f(a, b)
  return pair

def test_solve():
	assert car(cons(3, 4)) == 3
	assert cdr(cons(3, 4)) == 4
