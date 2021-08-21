# Evaluate Expression

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

Don't use `eval` or a similar built-in parser.

## Examples

| Input                   | Output |
| ----------------------- | ------ |
| `'1 + 2 + 3 + 4 + 5'`   | `15`   |
| `'-1 + (2 + 3)'`        | `4`    |
| `'1 + 5 * 2'`           | `11`   |
| `'(1 + 5) * 2'`         | `12`   |
| `'1 + (5 + (10 -2))'`   | `14`   |
| `'1 + (5 + (10 + -2))'` | `14`   |
| `'1 + (5 + (10 * -2))'` | `-14`  |
| `'1 + (5 + (10 * 2))'`  | `26`   |
