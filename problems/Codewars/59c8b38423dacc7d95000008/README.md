[_metadata_:generated]: - "true"

# Simple Fun #352: Reagent Formula

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59c8b38423dacc7d95000008`](https://www.codewars.com/kata/59c8b38423dacc7d95000008) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Now we will confect a reagent. There are eight materials to choose from, numbered 1,2,..., 8 respectively.

We know the rules of confect:
```
material1 and material2 cannot be selected at the same time
material3 and material4 cannot be selected at the same time
material5 and material6 must be selected at the same time
material7 or  material8 must be selected(at least one, or both)
```

# Task

You are given a integer array `formula`. Array contains only digits 1-8 that represents material 1-8. Your task is to determine if the formula is valid. Returns `true` if it's valid, `false` otherwise.


# Example

For `formula = [1,3,7]`, The output should be `true`.

For `formula = [7,1,2,3]`, The output should be `false`.

For `formula = [1,3,5,7]`, The output should be `false`.

For `formula = [1,5,6,7,3]`, The output should be `true`.

For `formula = [5,6,7]`, The output should be `true`.

For `formula = [5,6,7,8]`, The output should be `true`.

For `formula = [6,7,8]`, The output should be `false`.

For `formula = [7,8]`, The output should be `true`.


# Note

- All inputs are valid. Array contains at least 1 digit. Each digit appears at most once. 

- Happy Coding `^_^`

