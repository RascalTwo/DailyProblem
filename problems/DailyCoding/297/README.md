# Common Elements

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set.

A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize.

Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be `2`, as drinks `1` and `5` will satisfy everyone.

## Examples

In the following situation, customer `0` will be satisfied with drinks `0`, `1`, `3`, or `6`.

    {
        0: [0, 1, 3, 6],
        1: [1, 4, 7],
        2: [2, 4, 7, 5],
        3: [3, 2, 5],
        4: [5, 8]
    }

| Input                                                                       | Output   |
| --------------------------------------------------------------------------- | -------- |
| `{0: [0, 1, 3, 6], 1: [1, 4, 7], 2: [2, 4, 7, 5], 3: [3, 2, 5], 4: [5, 8]}` | `{1, 5}` |
