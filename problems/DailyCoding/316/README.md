# Determine Denominations

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given an array of length `N`, where each element `i` represents the number of ways we can produce `i` units of change.

Given such an array, determine the denominations that must be in use.

## Examples

`[1, 0, 1, 1, 2]` would indicate that there is only one way to make `0`, `2`, or `3` units, and `2` ways of making `4` units.

There must be coins with value `2`, `3`, and `4`.

| Input             | Output         |
| ----------------- | -------------- |
| `[1, 0, 1, 1, 2]` | `[1, 2, 3, 4]` |
