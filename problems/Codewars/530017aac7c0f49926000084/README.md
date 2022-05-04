[_metadata_:generated]: - "true"

# Pluck

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`530017aac7c0f49926000084`](https://www.codewars.com/kata/530017aac7c0f49926000084) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Implement a function which takes a sequence of objects and a property name, and returns a sequence containing the named property of each object.

For example:
```javascript
pluck([{a:1}, {a:2}], 'a')      // -> [1,2]
pluck([{a:1, b:3}, {a:2}], 'b') // -> [3, undefined]
```

```python
pluck([{'a':1}, {'a':2}], 'a')        # -> [1,2]
pluck([{'a':1, 'b':3}, {'a':2}], 'b') # -> [3, None]
```

If an object is missing the property, you should just leave it as `undefined/None` in the output array.
