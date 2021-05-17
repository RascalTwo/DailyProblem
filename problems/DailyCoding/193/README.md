# Optimal Stock Market Transactions

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock.

You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

## Examples

Given `[1, 3, 2, 8, 4, 10]` and `fee = 2`, you should return `9`, since you could buy the stock at `1` dollar, and sell at `8` dollars, and then buy it at `4` dollars and sell it at `10` dollars.

Since we did two transactions, there is a `4` dollar fee, so we have `7 + 6 = 13` profit minus `4` dollars of fees.

| Input                 | Output |
| --------------------- | ------ |
| `[1, 3, 2, 8, 4, 10]` | `9`    |
