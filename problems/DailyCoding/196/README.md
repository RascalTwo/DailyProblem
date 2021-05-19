# Most Frequent Binary Subtree Sum

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given the root of a binary tree, find the most frequent subtree sum.

> The subtree sum of a node is the sum of all values under a node, including the node itself.

## Examples

Given the following tree:

      5
     / \
    2  -5

Return `2` as it occurs twice: once as the left leaf, and once as the sum of `2 + 5 - 5`.

| Input                                                 | Output |
| ----------------------------------------------------- | ------ |
| `Node(5, Node(2), Node(-5)))`                         | `2`    |
| `Node(0, Node(2, Node(3)), Node(-5, None, Node(7))))` | `7`    |
