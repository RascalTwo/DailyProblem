# Calculate Equation Variable Values

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a series of arithmetic equations as strings

The equations use addition only and are separated by newlines.

Return a mapping of all variables to their values.

If it's not possible, then return `None`.

## Examples

Given these three expressions:

    y = x + 1
    5 = x + 3
    10 = z + y + 2

you should return `{ x: 2, y: 3, z: 5 }`

| Input                                    | Output                 |
| ---------------------------------------- | ---------------------- |
| `'y = x + 1\n5 = x + 3\n10 = z + y + 2'` | `{ x: 2, y: 3, z: 5 }` |
