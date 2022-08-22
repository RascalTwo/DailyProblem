[_metadata_:generated]: - "true"

# Simple frequency sort

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a8d2bf60025e9163c0000bc`](https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this Kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value. 

```haskell
solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
--we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
```

```cpp
solve({2,3,5,3,7,9,5,3,7}) == {3,3,3,5,5,7,7,2,9}
// We sort by highest frequency to lowest frequency.
// If two elements have same frequency, we sort by increasing value.
```

```java
Solution.sortByFrequency(new int[]{2, 3, 5, 3, 7, 9, 5, 3, 7});
// Returns {3, 3, 3, 5, 5, 7, 7, 2, 9}
// We sort by highest frequency to lowest frequency.
// If two elements have same frequency, we sort by increasing value.
```

More examples in test cases. 

Good luck!

Please also try [Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)
