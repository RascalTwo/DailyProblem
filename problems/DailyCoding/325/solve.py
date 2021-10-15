import fractions
import collections
import operator

from typing import Any, Callable, DefaultDict, Dict, Optional, Tuple, Union



Operation = Callable[[Any, Any], Any]

class UnitConverter:
	def __init__(self):
		self.conversions: DefaultDict[str, Dict[str, Tuple[Operation, fractions.Fraction]]] = collections.defaultdict(dict)


	def add(self, origin: str, to: str, op: Operation, formula: fractions.Fraction, invert: Optional[Operation] = None) -> 'UnitConverter':
		self.conversions[to][origin] = (op, formula)
		if invert:
			self.conversions[origin][to] = (invert, formula)
		return self


	def convert(self, origin: str, to: str, value: Union[str, int, float, fractions.Fraction]):
		if not isinstance(value, fractions.Fraction):
			value = fractions.Fraction(value)

		if to not in self.conversions[origin]:
			raise Exception(f'Unit conversion not found: "{origin}" to "{to}"')

		op, formula = self.conversions[origin][to]
		return op(value, formula)



def test_solve():
	instance = (
		UnitConverter()
			.add('inch', 'foot', operator.mul, fractions.Fraction(12, 1), operator.truediv)
	)
	assert instance.convert('inch', 'foot', fractions.Fraction(12, 1)) == 1
	assert instance.convert('foot', 'inch', fractions.Fraction(1, 1)) == 12
	assert instance.convert('foot', 'inch', '1') == 12
	assert instance.convert('foot', 'inch', 1.5) == 18
