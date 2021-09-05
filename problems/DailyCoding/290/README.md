# Count Quxes Transformations

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

On a mysterious island there are creatures known as Quxes which come in three colors: `red`, `green`, and `blue`.

One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given `N` Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input `['R', 'G', 'B', 'G', 'B']`, it is possible to end up with a single Qux through the following steps:

| Arrangement               | Change      |
| ------------------------- | ----------- |
| ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B |
| ['B', 'B', 'G', 'B']      | (B, G) -> R |
| ['B', 'R', 'B']           | (R, B) -> G |
| ['B', 'G']                | (B, G) -> R |
| ['R']                     |             |

## Examples

| Input                       | Output |
| --------------------------- | ------ |
| `['R', 'G', 'B', 'G', 'B']` | `10`   |
