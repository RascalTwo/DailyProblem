[_metadata_:generated]: - "true"

# Rotate an array matrix

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`525a566985a9a47bc8000670`](https://www.codewars.com/kata/525a566985a9a47bc8000670) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a `rotate` function that rotates a two-dimensional array (a matrix)  either clockwise or anti-clockwise by 90 degrees, and  returns the rotated array.

The function accepts two parameters: an array, and a string specifying the direction or rotation. The direction will be either `"clockwise"` or `"counter-clockwise"`.

Here is an example of how your function will be used:

```javascript
var matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]];

rotate(matrix, "clockwise"); // Would return  [[7, 4, 1], [8, 5, 2],  [9, 6, 3]]
```
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate(matrix, "clockwise") #  Would return  [[7, 4, 1], [8, 5, 2],  [9, 6, 3]]
```
To help you visualize the rotated matrix, here it is formatted as a grid:

```javascript
 [[7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]]
```
```python
 [[7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]]
```
Rotated counter-clockwise it would looks like this:

```javascript
 [[3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]]
```
```python
 [[3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]]
```
