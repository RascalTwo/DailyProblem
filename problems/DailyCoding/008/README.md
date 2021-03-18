# Count Unival Trees

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

## Examples

The following tree has `5` unival subtrees:

       0
      / \
     1   0
        / \
       1   0
      / \
     1   1

| Input                                                           | Output |
| --------------------------------------------------------------- | ------ |
| `Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))` | `5`    |
| `Node(0, Node(0), Node(0)`                                      | `3`    |
| `Node(0, Node(1), Node(0))`                                     | `2`    |
| `Node(0, Node(0, Node(0)), Node(0))`                            | `4`    |
| `Node(0, Node(1, Node(0)), Node(0))`                            | `2`    |
| `Node(0, Node(0, Node(1)))`                                     | `1`    |
