# Find Transitive Closure

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

The transitive closure of a graph is a measure of which vertices are reachable from other vertices.

It can be represented as a matrix `M`, where `M[i][j] == 1` if there is a path between vertices `i` and `j`, and otherwise `0`.

Given a graph, find its transitive closure.

## Examples

Given the following graph in adjacency list form:

    [
        [0, 1, 3],
        [1, 2],
        [2],
        [3]
    ]

The transitive closure of this graph would be:

    [
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

| Input                           | Output                                                     |
| ------------------------------- | ---------------------------------------------------------- |
| `[[0, 1, 3], [1, 2], [2], [3]]` | `[[1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]` |
