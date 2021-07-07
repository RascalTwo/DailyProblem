# Relative Cardinal Position Validator

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A rule looks like this:

    A NE B

This means this means point `A` is located northeast of point `B`, while this:

    A SW C

means that point `A` is southwest of `C`.

Given a list of rules, check if the sum of the rules validate.

## Examples

    A N B
    B NE C
    C N A

does not validate, as `A` cannot be both north and south of `C`.

| Input                                                                                       | Output  |
| ------------------------------------------------------------------------------------------- | ------- |
| `['A NE B']`                                                                                | `True`  |
| `['N N C', 'NE NE C', 'E E C', 'SE SE C', 'S S C', 'SW SW C', 'W W C', 'NW NW C']`          | `True`  |
| `['N N C', 'NE NE C', 'E E C', 'SE SE C', 'S S C', 'SW SW C', 'W W C', 'NW NW C', 'S N N']` | `False` |
| `['A N B', 'C N A']`                                                                        | `True`  |
| `['C N A', 'A N B']`                                                                        | `True`  |
| `['A SW C']`                                                                                | `True`  |
| `['A N B', 'B NE C', 'C N A']`                                                              | `False` |
| `['A NW B', 'A N B']`                                                                       | `True`  |
