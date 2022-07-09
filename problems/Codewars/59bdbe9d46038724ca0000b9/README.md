[_metadata_:generated]: - "true"

# Pure Functions

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59bdbe9d46038724ca0000b9`](https://www.codewars.com/kata/59bdbe9d46038724ca0000b9) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

A function is <b>pure</b> when:

- It always return the same value given the same arguments (it doesn't update or depend on out of the scope variables);
- Evaluation of the result does not cause side effect (mutations...) or output


## Task

You are given a function that is impure, and your job is to purify it. This function must return a new array where each value is itself plus 2 times the "modifier", which is provided as a property of the `options` object.

Example:

```
Array = 1, 2, 3
Modifier = 5

Should return = 11, 12, 13
```
