[_metadata_:generated]: - "true"

# Day of the Year

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a1ebe0d46d843454100004c`](https://www.codewars.com/kata/5a1ebe0d46d843454100004c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Work out what number day of the year it is.

```
toDayOfYear([1, 1, 2000]) => 1
```
The argument passed into the function is an array with the format `[D, M, YYYY]`, e.g. `[1, 2, 2000]` for February 1st, 2000 or `[22, 12, 1999]` for December 22nd, 1999.

Don't forget to check for whether it's a [leap year](https://en.wikipedia.org/wiki/Leap_year)! Three criteria must be taken into account to identify leap years:
- The year can be evenly divided by 4;
- If the year can be evenly divided by 100, it is NOT a leap year, unless;
- The year is also evenly divisible by 400. Then it is a leap year.

