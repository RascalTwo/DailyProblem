[_metadata_:generated]: - "true"

# Dictionary from two lists

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5533c2a50c4fea6832000101`](https://www.codewars.com/kata/5533c2a50c4fea6832000101) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

There are two lists, possibly of different lengths. The first one consists of keys, the second one consists of values. Write a function ```createDict(keys, values)``` that returns a dictionary created from keys and values. If there are not enough values, the rest of keys should have a ```None``` (**JS** `null`)value. If there not enough keys, just ignore the rest of values.

Example 1:
```python
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}
```
```javascript
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
createDict(keys, values) // returns {'a': 1, 'b': 2, 'c': 3, 'd': null}
```

Example 2:
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}
```
```javascript
keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
createDict(keys, values) // returns {'a': 1, 'b': 2, 'c': 3}
```

