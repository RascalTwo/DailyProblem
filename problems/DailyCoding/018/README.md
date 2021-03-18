# Subarray Maximums

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an array of integers and a number `k`, where `1 <= k <= length of the array`, compute the maximum values of each subarray of length `k`.

## Examples

Given `array = [10, 5, 2, 7, 8, 7]` and `k = 3`, we should get: `[10, 7, 8, 8]`, since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

| Input                                                                                                  | Output          |
| ------------------------------------------------------------------------------------------------------ | --------------- |
| <table><tr><th>integers</th><th>k</th></tr><tr><td>`[10, 5, 2, 7, 8, 7]`</td><td>`3`</td></tr></table> | `[10, 7, 8, 8]` |
