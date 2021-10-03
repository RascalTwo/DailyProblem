# Domino/Tromino Packing

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a `2 x N` board, and instructed to completely cover the board with the following shapes:

- `Dominoes`, or `2 x 1` rectangles.
- `Trominoes`, or `L`-shapes.

## Examples

If `N = 4`, here is one possible configuration, where `A` is a `domino`, and `B` and `C` are `trominoes`.

    A B B C
    A B C C

Given an integer `N`, determine in how many ways this task is possible.

| Input | Output |
| ----- | ------ |
| `2`   | `2`    |
| `4`   | `14`   |
| `5`   | `42`   |
