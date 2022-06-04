[_metadata_:generated]: - "true"

# Concatenated Sum

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59a1ec603203e862bb00004f`](https://www.codewars.com/kata/59a1ec603203e862bb00004f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The number `198` has the property that `198 = 11 + 99 + 88, i.e., if each of its digits is concatenated twice and then summed, the result will be the original number`. It turns out that `198` is the only number with this property. However, the property can be generalized so that each digit is concatenated `n` times and then summed. 

## Examples
```
original number =2997 , n=3
2997 = 222+999+999+777 and here each digit is concatenated three times.

original number=-2997 , n=3

-2997 = -222-999-999-777 and here each digit is concatenated three times.
```
## Task

```if:python
Write a function named `check_concatenated_sum` that tests if a number has this generalized property.
```
```if-not:python
Write a function named `checkConcatenatedSum` that tests if a number has this generalized property.
```

