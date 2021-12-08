# JSON encoder

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Write a function that takes in a `number`, `string`, `list`, or `dictionary` and returns its JSON encoding.

It should also handle `nulls`.

## Examples

| Input                                | Output                                  |
| ------------------------------------ | --------------------------------------- |
| `[None, 123, ["a", "b"], {"c":"d"}]` | `'[null, 123, ["a", "b"], {"c": "d"}]'` |
