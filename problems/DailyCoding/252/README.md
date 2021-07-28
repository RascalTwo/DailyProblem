# Egyptian Fractions

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, `4 / 13` can be represented as `1 / 4 + 1 / 18 + 1 / 468`.

Create an algorithm to turn an ordinary fraction `a / b`, where `a < b`, into an Egyptian fraction.

## Examples

| Input                                                                           | Output         |
| ------------------------------------------------------------------------------- | -------------- |
| <table><tr><th>a</th><th>b</th></tr><tr><td>`5`</td><td>`8`</td></tr></table>   | `[2, 8]`       |
| <table><tr><th>a</th><th>b</th></tr><tr><td>`13`</td><td>`12`</td></tr></table> | `[2, 3, 4]`    |
| <table><tr><th>a</th><th>b</th></tr><tr><td>`4`</td><td>`13`</td></tr></table>  | `[4, 18, 468]` |
