# Forex Trading Profit Detection

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a table of currency exchange rates, represented as a 2D array.

Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount `A` of any currency, so that you can end up with some amount greater than `A` of that currency.

There are no transaction costs and you can trade fractional quantities.

## Examples

| Input                                                                     | Output                 |
| ------------------------------------------------------------------------- | ---------------------- |
| `{ 'A': {'B': 1}, 'B': {'A': 1, 'C': 0.95}, 'C': {'A': 1.1, 'B': 1.05} }` | `['A', 'B', 'C', 'A']` |
| `{ 'A': {'B': 1}, 'B': {'A': 1, 'C': 0.1}, 'C': {'A': 1.1, 'B': 1.1} }`   | `None`                 |
