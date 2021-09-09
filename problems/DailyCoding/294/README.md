# Shortest Parabolic Path

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A competitive runner would like to create a route that starts and ends at his house, with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form `{location: elevation}`, and a dictionary mapping paths between some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above.

Assume the runner's home is location `0`.

## Examples

Suppose you are given the following input:

    elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
    paths = {
        (0, 1): 10,
        (0, 2): 8,
        (0, 3): 15,
        (1, 3): 12,
        (2, 4): 10,
        (3, 4): 5,
        (3, 0): 17,
        (4, 0): 10
    }

In this case, the shortest valid path would be `0 -> 2 -> 4 -> 0`, with a distance of `28`.

| Input                                                                                                                                                                                                                    | Output   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| <table><tr><th>elevations</th><th>paths</th></tr><tr><td>`{0: 5, 1: 25, 2: 15, 3: 20, 4: 10}`</td><td>`{(0, 1): 10, (0, 2): 8, (0, 3): 15, (1, 3): 12, (2, 4): 10, (3, 4): 5, (3, 0): 17, (4, 0): 10}`</td></tr></table> | `[0, 3]` |
