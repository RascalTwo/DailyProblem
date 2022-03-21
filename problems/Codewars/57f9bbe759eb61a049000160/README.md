[_metadata_:generated]: - "true"

# Guess the Digits and Expression

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57f9bbe759eb61a049000160`](https://www.codewars.com/kata/57f9bbe759eb61a049000160) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Description:
Give you a multiplication arithmetic expression:

```
                ABC
            *   CBA
            -------
            = 39483
```
Each character represents a diffrent digit(1-9), and you need to find the arithmetic expression and return the result like this: 

```
"123 * 321 = 39483"
```
You can assume that the first line always contains all the digits that you need to guess. You can assume that all testcase always has one or more than one valid results. If more than one valid result exists, choose the one which has the smallest first number. In the example above, `"321 * 123 = 39483"` is also a valid result, but 321 > 123.

# Examples

```
exp=
`    ABC
*   CBA
-------
= 39483`
guessExpression(exp) === "123 * 321 = 39483"

exp=
`  AAA
*   A
------
= 444`
guessExpression(exp) === "222 * 2 = 444"

exp=
`   AB
* ABA
------
= 1452`
guessExpression(exp) === "12 * 121 = 1452"

exp = 
`        BCEAD
*      AEDBCA
--------------
= 13300171373`
guessExpression(exp) === "92413 * 143921 = 13300171373"
```

