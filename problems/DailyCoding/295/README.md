# Pascal's Triangle

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number `1`.

For each subsequent row, each element is the sum of the numbers directly above it, on either side.

For example, here are the first few rows:

        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1

Given an input `k`, return the kth row of Pascal's triangle.

## Examples

| Input | Output            |
| ----- | ----------------- |
| `3`   | `[1, 3, 3, 1]`    |
| `4`   | `[1, 4, 6, 4, 1]` |
