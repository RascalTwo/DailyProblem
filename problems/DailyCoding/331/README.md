# Minimum Flips to unblock

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a string consisting of the letters `x` and `y`, such as `xyxxxyxyy`.

In addition, you have an operation called flip, which changes a single `x` to `y` or vice versa.

Determine how many times you would need to apply this operation to ensure that all `x`'s come before all `y`'s.

## Examples

Given `xyxxxyxyy`, it suffices to flip the second and sixth characters, so you should return `2`.

| Input          | Output         |
| -------------- | -------------- |
| `'xyxxxyxyy'`  | `[1, 5]`       |
| `'yyyyyyyyy'`  | `[]`           |
| `'yyyyyyyyx'`  | `[8]`          |
| `'xxxxxyyyx'`  | `[8]`          |
| `'xyxyxyxyxy'` | `[1, 3, 5, 7]` |
