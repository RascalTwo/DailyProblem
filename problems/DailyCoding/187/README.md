# Overlapping Rectangles

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given given a list of rectangles represented by min and max x- and y-coordinates.

Compute whether or not a pair of rectangles overlap each other.

If one rectangle completely covers another, it is considered overlapping.

## Examples

Given the following rectangles:

    {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    }, {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    }, {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }

return `True` as the first and third rectangle overlap each other.

| Input                                                                                                                                      | Output  |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `[{ "top_left": (1, 4), "dimensions": (3, 3)}, { "top_left": (-1, 3), "dimensions": (2, 1)}, { "top_left": (0, 5), "dimensions": (4, 3)}]` | `True`  |
| `[{ "top_left": (1, 4), "dimensions": (3, 3)}, { "top_left": (-1, 3), "dimensions": (2, 1)}]`                                              | `False` |
