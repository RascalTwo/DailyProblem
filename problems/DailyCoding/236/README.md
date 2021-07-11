# Point within Polygon

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a list of `N` points `(x1, y1), (x2, y2), ..., (xN, yN)` representing a polygon.

You can assume these points are given in order; that is, you can construct the polygon by connecting point `1` to point `2`, point `2` to point `3`, and so on, finally looping around to connect point `N` to point `1`.

Determine if a new point `p` lies inside this polygon. (If `p` is on the boundary of the polygon, you should return `False`).

## Examples

| Input                                                                                                                                   | Output  |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| <table><tr><th>polygon</th><th>point</th></tr><tr><td>`[(3, -8), (6, 5), (4, 8), (-3, 4), (-6, -4)]`</td><td>`(0, 0)`</td></tr></table> | `True`  |
| <table><tr><th>polygon</th><th>point</th></tr><tr><td>`[(3, -8), (6, 5), (4, 8), (-3, 4), (-6, -4)]`</td><td>`(3, 6)`</td></tr></table> | `True`  |
| <table><tr><th>polygon</th><th>point</th></tr><tr><td>`[(3, -8), (6, 5), (4, 8), (-3, 4), (-6, -4)]`</td><td>`(6, 3)`</td></tr></table> | `False` |
