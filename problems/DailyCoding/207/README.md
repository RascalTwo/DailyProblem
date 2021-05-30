# Bipartite Graph

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an undirected graph `G`, check whether it is bipartite.

Recall that a graph is bipartite if its vertices can be divided into two independent sets, `U` and `V`, such that no edge connects vertices of the same set.

## Examples

| Input                                                                                                                        | Output  |
| ---------------------------------------------------------------------------------------------------------------------------- | ------- |
| `[ [0, 1], [1, 0] ]`                                                                                                         | `True`  |
| `[ [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0] ]`                                                                 | `True`  |
| `[ [0, 0, 1, 1], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0] ]`                                                                 | `False` |
| `[ [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0] ]` | `True`  |
| `[ [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0] ]` | `False` |
