# Calculate Trapped Water

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height.

Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map.

## Examples

Given the input `[2, 1, 2]`, we can hold `1` unit of water in the middle.

Given the input `[3, 0, 1, 3, 0, 5]`, we can hold `3` units in the first index, `2` in the second, and `3` in the fourth index (we cannot hold `5` since it would run off to the left), so we can trap `8` units of water.

| Input                | Output |
| -------------------- | ------ |
| `[2, 1, 2]`          | `1`    |
| `[3, 0, 1, 3, 0, 5]` | `8`    |
| `[3, 0, 1, 5, 0, 5]` | `8`    |
