[_metadata_:generated]: - "true"

# Alternating Loops

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55e529bf6c6497394a0000b5`](https://www.codewars.com/kata/55e529bf6c6497394a0000b5) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write

```javascript
function combine()
```
```python
function combine()
```
```ruby
function combine()
```
```haskell
combine :: [[a]] -> [a]
```

that combines arrays by alternatingly taking elements passed to it.

E.g

```javascript
combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
```
```python
combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
```
```ruby
combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
```
```haskell
combine [[1, 2, 3], [1, 2, 3]]                    == [1, 1, 2, 2, 3, 3]
combine [[1, 2, 3], [1, 2, 3, 4, 5]]              == [1, 1, 2, 2, 3, 3, 4, 5]
combine [[1, 2, 3], [1, 2, 3, 4, 5], [6, 7], [8]] == [1, 1, 6, 8, 2, 2, 7, 3, 3, 4, 5]
```

Arrays can have different lengths.
