# Identify the Celebrity

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity").

To help figure out who this is, you have access to an `O(1)` method called `knows(a, b)`, which returns `True` if person `a` knows person `b`, else `False`.

Given a list of `N` people and the above operation, find a way to identify the celebrity in `O(N)` time.

## Examples

| Input                                                                                                                             | Output |
| --------------------------------------------------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>people</th><th>celebrity</th></tr><tr><td>`['a', 'b', 'c', 'd', 'E', 'f', 'g', 'h']`</td><td>`E`</td></tr></table> | `E`    |
| <table><tr><th>people</th><th>celebrity</th></tr><tr><td>`['a', 'b', 'c', 'd', 'E', 'f', 'g', 'h']`</td><td>`G`</td></tr></table> | `None` |
