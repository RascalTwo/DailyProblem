# Generate Preferential Playlist

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You have access to ranked lists of songs for various users.

Each song is represented as an integer, and more preferred songs appear earlier in each list.

The list `[4, 1, 7]` indicates that a user likes song `4` the best, followed by songs `1` and `7`.

Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.

## Examples

| Input                                     | Output                  |
| ----------------------------------------- | ----------------------- |
| `[[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]` | `[2, 1, 6, 7, 3, 9, 5]` |
