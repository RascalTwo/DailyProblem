# Equally-summable Partitions

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

## Examples

Given the multiset `{15, 5, 20, 10, 35, 15, 10}`, it would return `true`, since we can split it up into `{15, 5, 10, 15, 10}` and `{20, 35}`, which both add up to `55`.

Given the multiset `{15, 5, 20, 10, 35}`, it would return `false`, since we can't split it up into two subsets that add up to the same sum.

| Input                         | Output  |
| ----------------------------- | ------- |
| `[15, 5, 20, 10, 35, 15, 10]` | `True`  |
| `[15, 5, 20, 10, 35]`         | `False` |
