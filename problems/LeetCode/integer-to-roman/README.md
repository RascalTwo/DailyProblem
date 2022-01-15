# Integer to Roman

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                               | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------: | :------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`integer-to-roman`](https://leetcode.com/problems/integer-to-roman) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

    {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

In addition, note that the Roman numeral system uses subtractive notation for numbers such as `IV` and `XL`.

## Examples

| Input  | Output      |
| ------ | ----------- |
| `1666` | `'MDCLXVI'` |
| `14`   | `'XIV'`     |
| `13`   | `'XIII'`    |
| `20`   | `'XX'`      |
| `9`    | `'IX'`      |
| `40`   | `'XL'`      |
| `39`   | `'XXXIX'`   |
| `8`    | `'VIII'`    |
| `2`    | `'II'`      |
| `4`    | `'IV'`      |
