# Calculate H-Index

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

In academia, the `h`-index is a metric used to calculate the impact of a researcher's papers.

It is calculated as follows:

- A researcher has index `h` if at least `h` of her `N` papers have `h` citations each.
- If there are multiple `h` satisfying this formula, the maximum is chosen.

Given a list of paper citations of a researcher, calculate their `h`-index.

## Examples

Suppose citations of each paper are `[4, 3, 0, 1, 5]`.

Then the h-index would be `3`, since the researcher has `3` papers with at least `3` citations.

| Input             | Output |
| ----------------- | ------ |
| `[4, 3, 0, 1, 5]` | `3`    |
