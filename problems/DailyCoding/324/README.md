# Shortest Multiple Paths

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Consider the following scenario: there are `N` mice and `N` holes placed at integer points along a line.

Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the `left` or `right`, and only one mouse can fit inside each hole.

## Examples

Suppose the mice are positioned at `[1, 4, 9, 15]`, and the holes are located at `[10, -5, 0, 16]`.

In this case, the best pairing would require us to send the mouse at `1` to the hole at `-5,` so our function should return `6`.

| Input                                                                                                          | Output                           |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| <table><tr><th>mice</th><th>holes</th></tr><tr><td>`[1, 4, 9, 15]`</td><td>`[10, -5, 0, 16]`</td></tr></table> | `{ 1: -5, 4: 0, 9: 10, 15: 16 }` |
