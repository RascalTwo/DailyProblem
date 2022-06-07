[_metadata_:generated]: - "true"

# Number of trailing zeros of N!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52f787eb172a8b4ae1000a34`](https://www.codewars.com/kata/52f787eb172a8b4ae1000a34) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

`N! = 1 * 2 * 3 *  ... * N`

Be careful `1000!` has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html 

## Examples

```python
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
```

*Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.*
