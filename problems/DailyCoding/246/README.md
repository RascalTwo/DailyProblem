# Circular Words

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a list of words, determine whether the words can be chained to form a circle.

A word `X` can be placed in front of another word `Y` in a circle if the last character of `X` is same as the first character of `Y`.

## Examples

| Input                                              | Output                                            |
| -------------------------------------------------- | ------------------------------------------------- |
| `['cat', 'taco']`                                  | `['cat', 'taco']`                                 |
| `['taco', 'cat']`                                  | `None`                                            |
| `['cat', 'opera', 'taco']`                         | `['cat', 'taco', 'opera']`                        |
| `['cat', 'omega', 'taco', 'alpha']`                | `['cat', 'taco', 'omega', 'alpha']`               |
| `['chair', 'height', 'racket', 'tunic', 'touch']`  | `['chair', 'racket', 'touch', 'height', 'tunic']` |
| `['chair', 'height', 'racket', 'tunic', 'touchy']` | `None`                                            |
