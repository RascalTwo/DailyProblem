[_metadata_:generated]: - "true"

# Sum of a sequence

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`586f6741c66d18c22800010a`](https://www.codewars.com/kata/586f6741c66d18c22800010a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: **begin**, **end**, **step (inclusive)**.

If **begin** value is greater than the **end**, function should returns **0**

**Examples**

~~~if-not:nasm
```
2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
```
~~~

```if:nasm
mov edi, 2
mov esi, 2
mov edx, 2
call sequence_sum    ; EAX <- 2

mov edi, 2
mov esi, 6
mov edx, 2
call sequence_sum    ; EAX <- 12 = 2 + 4 + 6

mov edi, 1
mov esi, 5
mov edx, 1
call sequence_sum    ; EAX <- 15 = 1 + 2 + 3 + 4 + 5

mov edi, 1
mov esi, 5
mov edx, 3
call sequence_sum    ; EAX <- 5 = 1 + 4
```

This is the first kata in the series:

1) Sum of a sequence (this kata)  
2) [Sum of a Sequence [Hard-Core Version]](https://www.codewars.com/kata/sum-of-a-sequence-hard-core-version/javascript)

