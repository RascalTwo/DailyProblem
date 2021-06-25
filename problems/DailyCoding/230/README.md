# Lowest floor to drop Egg

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given `N` identical eggs and access to a building with `k` floors.

Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor.

Once an egg breaks, it cannot be dropped again.

If an egg breaks when dropped from the `x`th floor, you can assume it will also break when dropped from any floor greater than `x`.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

## Examples

If `N = 1` and `k = 5`, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be `5`.

| Input                                                                                  | Output |
| -------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>eggs</th><th>floors</th></tr><tr><td>`1`</td><td>`5`</td></tr></table>  | `5`    |
| <table><tr><th>eggs</th><th>floors</th></tr><tr><td>`2`</td><td>`5`</td></tr></table>  | `3`    |
| <table><tr><th>eggs</th><th>floors</th></tr><tr><td>`2`</td><td>`10`</td></tr></table> | `4`    |
