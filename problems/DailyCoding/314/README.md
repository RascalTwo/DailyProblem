# Minimum Tower Range

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You are the technical director of WSPT radio, serving listeners nationwide.

For simplicity's sake we can consider each listener to live along a horizontal line stretching from `0` (west) to `1000` (east).

Given a list of `N` listeners, and a list of `M` radio towers, each placed at various locations along this line, determine what the minimum broadcast range would have to be in order for each listener's home to be covered.

## Examples

Suppose `listeners = [1, 5, 11, 20]`, and `towers = [4, 8, 15]`.

In this case the minimum range would be `5`, since that would be required for the tower at position `15` to reach the listener at position `20`.

    LL  --  --  --  LL  --  --  --  --  -- LL -- -- -- -- -- -- -- -- LL
    --  --  --  T T --  --  --  TT  --  -- -- -- -- -- TT -- -- -- -- --
    --  --  --  --  --  --  --  --  --  -- -- -- -- -- -- -- -- -- -- --
    01  02  03  04  05  06  07  08  09  10 11 12 13 14 15 16 17 18 19 20

| Input                                                                                               | Output |
| --------------------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>listeners</th><th>towers</th></tr><tr><td>`v`</td><td>`[4, 8, 15]`</td></tr></table> | `5`    |
