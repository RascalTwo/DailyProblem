# Find Bridge in Graph

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A bridge in a connected (undirected) graph is an edge that, if removed, causes the graph to become disconnected.

Find the bridge in a graph.

## Examples

| Input                                                                                  | Output         |
| -------------------------------------------------------------------------------------- | -------------- |
| `[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('C', 'D'), ('D', 'E')]`             | `[('D', 'E')]` |
| `[('A', 'B'), ('B', 'C'), ('C', 'A'), ('X', 'Y'), ('Y', 'Z'), ('Z', 'X'), ('C', 'X')]` | `[('C', 'X')]` |
