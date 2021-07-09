# Maximum Spanning Tree

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Recall that the minimum spanning tree is the subset of edges of a tree that connect all its vertices with the smallest possible total edge weight.

Given an undirected graph with weighted edges, compute the maximum weight spanning tree.

## Examples

| Input                                                                                                                                                                                             | Output                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `{ 'A': {'B': 1, 'D': 4, 'E': 3}, 'B': {'A': 1, 'D': 4, 'E': 2}, 'C': {'E': 4, 'F': 5}, 'D': {'A': 4, 'B': 4, 'E': 4}, 'E': {'A': 3, 'B': 2, 'C': 4, 'D': 4, 'F': 7}, 'F': {'C': 5, 'E': 7}}`     | `[('E', 'F'), ('C', 'F'), ('A', 'D'), ('B', 'D'), ('D', 'E')]` |
| `{ 'A': {'B': 100, 'D': 4, 'E': 3}, 'B': {'A': 100, 'D': 4, 'E': 2}, 'C': {'E': 4, 'F': 5}, 'D': {'A': 4, 'B': 4, 'E': 4}, 'E': {'A': 3, 'B': 2, 'C': 4, 'D': 4, 'F': 7}, 'F': {'C': 5, 'E': 7}}` | `[('A', 'B'), ('E', 'F'), ('C', 'F'), ('A', 'D'), ('D', 'E')]` |
