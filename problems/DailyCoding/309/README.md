# Least Disruptive Gapless-Reseating

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

There are `M` people sitting in a row of `N` seats, where `M` < `N`.

Your task is to redistribute people such that there are no gaps between any of them, while keeping overall movement to a minimum.

We can consider the cost of a solution to be the sum of the absolute distance each person must move, so that the cost here would be `five`.

Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.

## Examples

Suppose you are faced with an input of `[0, 1, 1, 0, 1, 0, 0, 0, 1]`, where `0` represents an empty seat and `1` represents a person.

In this case, one solution would be to place the person on the right in the fourth seat.

| Input                                           | Output |
| ----------------------------------------------- | ------ |
| `[0, 1, 1, 0, 1, 0, 0, 0, 1]`                   | `5`    |
| `[1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]` | `18`   |
