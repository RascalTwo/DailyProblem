[_metadata_:generated]: - "true"

# Diagonals sum

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5592fc599a7f40adac0000a8`](https://www.codewars.com/kata/5592fc599a7f40adac0000a8) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

 Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary)

> Matrix = array of `n` length whose elements are `n` length arrays of integers.

3x3 example:

```javascript
diagonals( [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ); 

returns -> 30 // 1 + 5 + 9 + 3 + 5 + 7
```
```python
sum_diagonals( [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ) == 30 # 1 + 5 + 9 + 3 + 5 + 7
```

