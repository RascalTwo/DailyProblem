[_metadata_:generated]: - "true"

# Compare Strings by Sum of Chars

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`576bb3c4b1abc497ec000065`](https://www.codewars.com/kata/576bb3c4b1abc497ec000065) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Compare two strings by comparing the sum of their values (ASCII character code).

* For comparing treat all letters as UpperCase
* `null/NULL/Nil/None` should be treated as empty strings
* If the string contains other characters than letters, treat the whole string as it would be empty

Your method should return `true`, if the strings are equal and `false` if they are not equal.

## Examples:
```
"AD", "BC"  -> equal
"AD", "DD"  -> not equal
"gf", "FG"  -> equal
"zz1", ""   -> equal (both are considered empty)
"ZzZz", "ffPFF" -> equal
"kl", "lz"  -> not equal
null, ""    -> equal
```

