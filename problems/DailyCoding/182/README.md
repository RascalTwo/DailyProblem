# Minimally-Connected Graph Checker

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected.

Any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected.

## Examples

| Input                                                                                   | Output  |
| --------------------------------------------------------------------------------------- | ------- |
| `[[0, 1, 0, 0, 1], [1, 0, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 0]]` | `False` |
| `[[0, 1, 1], [0, 0, 0], [0, 0, 0]]`                                                     | `True`  |
