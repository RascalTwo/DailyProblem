# Integer Array Jumping

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given an array of nonnegative integers.

Let's say you start at the beginning of the array and are trying to advance to the end.

You can advance at most, the number of steps that you're currently on.

Determine whether you can get to the end of the array.

## Examples

Given the array `[1, 3, 1, 2, 0, 1]`, we can go from indices `0 -> 1 -> 3 -> 5`, so return `True`.

| Input                | Output  |
| -------------------- | ------- |
| `[2, 3, 1, 1, 4]`    | `True`  |
| `[1, 3, 1, 2, 0, 1]` | `True`  |
| `[1, 2, 1, 0, 0]`    | `False` |
| `[3, 1, 2, -2, 0]`   | `True`  |
