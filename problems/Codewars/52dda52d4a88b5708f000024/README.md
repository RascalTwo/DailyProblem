[_metadata_:generated]: - "true"

# Ordinal Numbers

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52dda52d4a88b5708f000024`](https://www.codewars.com/kata/52dda52d4a88b5708f000024) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

**Introduction**

Ordinal numbers are used to tell the position of something in a list. Unlike regular numbers, they have a special suffix added to the end of them.


**Task**

Your task is to write the `ordinal(number, brief)` function. `number` will be an integer. You need to find the ordinal suffix of said number.

`brief` is an optional parameter and defaults to `false`. When using brief notation, `nd` and `rd` use `d` instead. All others are the same.

`ordinal(number, brief)` should return a string containing those two characters (or one character) that would be tagged onto the end of the number.

The last two digits determine the ordinal suffix.

**Notation for general notation**
<pre>
0  1  2  3  4  5  6  7  8  9
th st nd rd th th th th th th
</pre>

**Notation for brief notation**
<pre>
0  1  2  3  4  5  6  7  8  9
th st d  d th th th th th th
</pre>

**However, when the last two digits of the number are 11, 12, or 13, `th` is used instead of `st`,`nd`,`rd` respectively.**

**Examples**
<pre>
*General
1 - 1st
2 - 2nd
3 - 3rd
5 - 5th
11- 11th
149 - 149th
903 - 903rd
</pre>
<pre>
*Brief
1 - 1st
2 - 2d
3 - 3d
5 - 5th
11- 11th
149 - 149th
903 - 903d
</pre>

**Notes**

- Numbers might be passed in replacement of booleans, so `false` may be passed in as `0` and true may be passed in as `1`.
