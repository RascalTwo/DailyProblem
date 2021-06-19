# Last-Removed from Circular Array

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

There are `N` prisoners standing in a circle, waiting to be executed.

The executions are carried out starting with the `k`th person, and removing every successive `k`th person going clockwise until there is no one left.

Given `N` and `k`, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

## Examples

If `N = 5` and `k = 2`, the order of executions would be `[2, 4, 1, 5, 3]`, so you should return `3`.

| Input                                                                               | Output |
| ----------------------------------------------------------------------------------- | ------ |
| <table><tr><th>length</th><th>k</th></tr><tr><td>`5`</td><td>`2`</td></tr></table>  | `3`    |
| <table><tr><th>length</th><th>k</th></tr><tr><td>`10`</td><td>`3`</td></tr></table> | `4`    |
