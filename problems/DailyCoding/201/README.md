# Pyramid Maximum Weight Path

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.

`[[1], [2, 3], [1, 5, 1]]` represents the triangle:

      1
     2 3
    1 5 1

We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row.

Write a program that returns the weight of the maximum weight path.

## Examples

| Input                                                       | Output |
| ----------------------------------------------------------- | ------ |
| `[[1], [2, 3], [1, 5, 1]]`                                  | `9`    |
| `[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]`   | `15`   |
| `[[1], [1, 1], [1, 1, 48], [1, 1, 1, 1], [1, 1, 49, 1, 1]]` | `100`  |
