[_metadata_:generated]: - "true"

# Adding ordinal indicator suffixes to numbers

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52dca71390c32d8fb900002b`](https://www.codewars.com/kata/52dca71390c32d8fb900002b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Finish the function ```numberToOrdinal```, which should take a number and return it as a string with the correct ordinal indicator suffix (in English).  That is:

* ```numberToOrdinal(1) ==> '1st'```
* ```numberToOrdinal(2) ==> '2nd'```
* ```numberToOrdinal(3) ==> '3rd'```
* ```numberToOrdinal(4) ==> '4th'```
* ```... and so on```

For the purposes of this kata, you may assume that the function will always be passed a non-negative integer.  If the function is given 0 as an argument, it should return '0' (as a string).

To help you get started, here is an excerpt from Wikipedia's page on [Ordinal Indicators](http://en.wikipedia.org/wiki/Ordinal_indicator#English): 

* st is used with numbers ending in 1 (e.g. 1st, pronounced first)
* nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
* rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
* As an exception to the above rules, all the "teen" numbers ending with 11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th, pronounced one hundred [and] twelfth)
* th is used for all other numbers (e.g. 9th, pronounced ninth).
