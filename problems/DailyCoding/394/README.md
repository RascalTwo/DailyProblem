# Binary Tree Path Sum

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a binary tree and an integer `k`, return whether there exists a root-to-leaf path that sums up to `k`.

## Examples

Given `k = 18` and the following binary tree:

        8
       / \
      4   13
     / \   \
    2   6   19

Return `True` since the path `8 -> 4 -> 6` sums to `18`.

| Input                                                                                                                                       | Output  |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| <table><tr><th>tree</th><th>target</th></tr><tr><td>`Node(8, Node(4, Node(2), Node(6)), Node(13, Node(19)))`</td><td>`18`</td></tr></table> | `True`  |
| <table><tr><th>tree</th><th>target</th></tr><tr><td>`Node(8, Node(4, Node(2), Node(6)), Node(13, Node(19)))`</td><td>`19`</td></tr></table> | `False` |
| <table><tr><th>tree</th><th>target</th></tr><tr><td>`Node(8, Node(4, Node(2), Node(6)), Node(13, Node(19)))`</td><td>`12`</td></tr></table> | `False` |
