# Maximum Histogram Area

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a histogram consisting of rectangles of different heights.

These heights are represented in an input list, such that `[1, 3, 2, 5]` corresponds to the following diagram:

          x
          x
      x   x
      x x x
    x x x x

Determine the area of the largest rectangle that can be formed only from the bars of the histogram.

## Examples

For the diagram above, for example, this would be `six`, representing the `2 x 3` area at the bottom right.

| Input           | Output |
| --------------- | ------ |
| `[1, 3, 2, 5]`  | `6`    |
| `[1, 1, 1, 1]`  | `4`    |
| `[1, 1, 1, 10]` | `10`   |
