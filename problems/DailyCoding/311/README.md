# Find Peak in Rotated Array

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a array that's sorted but rotated at some unknown pivot, in which all elements are distinct, find a "peak" element in `O(log N)` time.

An element is considered a peak if it is greater than both its left and right neighbors.

It is guaranteed that the first and last elements are lower than all others.

## Examples

| Input                            | Output |
| -------------------------------- | ------ |
| `[1, 2, 3, 1]`                   | `2`    |
| `[1, 2, 3, 4]`                   | `-1`   |
| `[8, 7, 6, 1, 4, 5, 3, 9, 8, 4]` | `7`    |
