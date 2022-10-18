[_metadata_:generated]: - "true"

# Array.diff hero

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`581fc49b55c3d2d83c0000f8`](https://www.codewars.com/kata/581fc49b55c3d2d83c0000f8) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You know about simple [Array.diff task](https://www.codewars.com/kata/array-dot-diff). Now try to solve enhanced version!

Your goal in this kata is to implement a difference function, which subtracts one list from another.

It should remove all values from list `a`, which are present in list `b`. 
Each element `x` in both arrays is integer and `0 ≤ x ≤ 25`. And lengths of arrays can reach `5 000 000` elements.

```javascript
arrayDiffVeryFast([1,2],[1]) == [2]
```

If a value is present in `b`, all of its occurrences must be removed from another:

```javascript
arrayDiffVeryFast([1,2,2,2,3],[2]) == [1,3]
```
