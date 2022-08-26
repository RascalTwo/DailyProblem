[_metadata_:generated]: - "true"

# Row of the odd triangle

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5d5a7525207a674b71aa25b5`](https://www.codewars.com/kata/5d5a7525207a674b71aa25b5) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a triangle of consecutive odd numbers:

```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
```

find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

```
odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]
```

**Note**: your code should be optimized to handle big inputs.

___

The idea for this kata was taken from this kata: [Sum of odd numbers](https://www.codewars.com/kata/sum-of-odd-numbers)
