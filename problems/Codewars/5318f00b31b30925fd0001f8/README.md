[_metadata_:generated]: - "true"

# Formatting a number as price

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5318f00b31b30925fd0001f8`](https://www.codewars.com/kata/5318f00b31b30925fd0001f8) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Your objective is to add formatting to a plain number to display it as price.

The function should return a string like this:
```javascript
var price = numberToPrice(13253.5123);
console.log(price); // 13,253.51
```

Numbers should use the standard comma for every 3 numbers and dot to separate the cents, cents need to be truncated to 2 decimals, in the case that the decimal part of the number is 1 character long or none you should add 0's so that the result will always have 2 decimal characters, the function will also evaluate negative numbers.

function should return a string `'NaN'` if the input is not a valid number
