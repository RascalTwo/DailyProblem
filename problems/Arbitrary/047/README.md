# Maze Directional Navigation

<!-- INFO TABLE BEGIN -->

| Provider                                          | Solutions                                                                                                                                        |
| :-----------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [Arbitrary](../../../docs/providers/Arbitrary.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

While exploring an ancient tomb for treasure, you've come across a room with strange symbols on the floor.

These symbols tell you which way you need to walk in order to pass through the room.

However, you're not certain whether it's possible to follow these directions and reach the end of the room.

You start on the square in the upper left, and need to reach the square marked "E".

From each square you must follow the direction on the square. The directions are as follows:

- `v`
  - move down
- `>`
  - move right
- `^`
  - move up
- `<`
  - move left

The path is guaranteed not to loop.

Write a function that determines if it is possible to reach the end of the room from the start position in the upper left.

## Examples

| Input                                                                                                                                                          | Output  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `[['>', '>', '>', '>', 'v'], ['v', '^', '>', '^', 'v'], ['>', '^', '^', '>', 'E']]`                                                                            | `True`  |
| `[['v', '>', 'v'], ['v', '^', '>'], ['<', '>', 'E']]`                                                                                                          | `False` |
| `[['v', '>', '>', 'v', '>'], ['>', '>', 'v', '>', '^'], ['^', '>', '>', '>', 'E']]`                                                                            | `True`  |
| `[['v', '>', '>', 'v'], ['v', '^', '>', '>'], ['v', '>', '>', 'v'], ['v', '^', '<', 'v'], ['>', '>', '^', 'E']]`                                               | `True`  |
| `[['>', '>', '>', '>', '>', '>', '>', '>', '>', 'v'], ['v', '^', '>', 'v', '<', '>', 'v', '<', '<', '<'], ['>', '^', 'v', '<', '^', '<', '<', '^', '>', 'E']]` | `False` |
| `[['>', '>', 'v', 'E', 'v'], ['v', '^', '>', '^', 'v'], ['>', '^', '^', '>', '>']]`                                                                            | `True`  |
| `[['>', '>', 'v', '>', 'v'], ['v', '^', '>', '^', 'v'], ['>', 'E', '^', '>', '>']]`                                                                            | `False` |
| `[['>', '>', 'v', '>', '^'], ['v', '^', '>', '^', 'v'], ['>', 'E', '^', '>', '>']]`                                                                            | `False` |
| `[['>', 'v', '>', '>', 'v', '^'], ['v', '<', '^', 'v', '<', 'E'], ['>', '>', '^', '>', '>', '^']]`                                                             | `True`  |
| `[['>', 'v', '>', '>', 'v', '^'], ['v', '<', '^', '^', '<', 'E'], ['>', '>', '^', '>', '>', '^']]`                                                             | `False` |
