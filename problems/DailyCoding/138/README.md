# Coins needed for Amount

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given an array of integers representing coin denominations and a total amount of money.

Write a function to compute the fewest number of coins needed to make up that amount.

> If it is not possible to make that amount, return `None`.

## Examples

| Input                                                                                                        | Output |
| ------------------------------------------------------------------------------------------------------------ | ------ |
| <table><tr><th>denominations</th><th>amount</th></tr><tr><td>`[1, 5, 10, 25]`</td><td>`16`</td></tr></table> | `3`    |
| <table><tr><th>denominations</th><th>amount</th></tr><tr><td>`[1, 5, 10]`</td><td>`56`</td></tr></table>     | `7`    |
| <table><tr><th>denominations</th><th>amount</th></tr><tr><td>`[5, 8`</td><td>`15`</td></tr></table>          | `3`    |
