# Most Frequent Weight Graph Path

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

In a directed graph, each node is assigned an uppercase letter.

We define a path's value as the number of most frequently-occurring letter along that path.

Given a graph with `n` nodes and `m` directed edges, return the largest value path of the graph.

If the largest value is infinite, then return `None`.

The graph is represented with a string and an edge list. The `i`-th character represents the uppercase letter of the `i`-th node.

Each tuple in the edge list `(i, j)` means there is a directed edge from the `i`-th node to the `j`-th node.

Self-edges are possible, as well as multi-edges.

## Examples

The following input graph:

    ABACA

    [(0, 1),
     (0, 2),
     (2, 3),
     (3, 4)]

Would have maximum value `3` using the path of vertices `[0, 2, 3, 4], (A, A, C, A)`.

The following input graph:

    A

    [(0, 0)]

| Input                                                                                                                      | Output |
| -------------------------------------------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>letters</th><th>edges</th></tr><tr><td>`ABACA`</td><td>`[(0, 1), (0, 2), (2, 3), (3, 4)]`</td></tr></table> | `3`    |
| <table><tr><th>letters</th><th>edges</th></tr><tr><td>`A`</td><td>`[(0, 0)]`</td></tr></table>                             | `None` |
