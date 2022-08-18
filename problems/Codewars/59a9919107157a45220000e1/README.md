[_metadata_:generated]: - "true"

# Find all occurrences of an element in an array

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59a9919107157a45220000e1`](https://www.codewars.com/kata/59a9919107157a45220000e1) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given an array (a list in Python) of integers and an integer `n`, find all occurrences of `n` in the given array and return another array containing all the index positions of `n` in the given array.

If `n` is not in the given array, return an empty array `[]`.

Assume that `n` and all values in the given array will always be integers.

Example:
```c
find_all(7, {6, 9, 3, 4, 3, 82, 11}, 3, *z)
// returns pointer to {2, 4}
// assigns array length to `*z`
```
```python
find_all([6, 9, 3, 4, 3, 82, 11], 3)
> [2, 4]
```
```javascript
findAll([6, 9, 3, 4, 3, 82, 11], 3) => [2, 4]
```
```csharp
Kata.FindAll(new int[] {6, 9, 3, 4, 3, 82, 11}, 3) => new int[] {2, 4}
```
```haskell
findAll [6, 9, 3, 4, 3, 82, 11]  3 = [2, 4]
```
```ruby
find_all([6, 9, 3, 4, 3, 82, 11], 3) = [2, 4]
```
```prolog
find_all([6, 9, 3, 4, 3, 82, 11], 3) = [2, 4]
```

