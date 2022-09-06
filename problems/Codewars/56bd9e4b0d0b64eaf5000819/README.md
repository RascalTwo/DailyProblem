[_metadata_:generated]: - "true"

# Combine objects

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56bd9e4b0d0b64eaf5000819`](https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Your task is to write a function that takes two or more objects and returns a new object which combines all the input objects. 

All input object properties will have only numeric values. Objects are combined together so that the values of matching keys are added together.

An example:

```javascript
const objA = { a: 10, b: 20, c: 30 }
const objB = { a: 3, c: 6, d: 3 }
combine(objA, objB) // Returns { a: 13, b: 20, c: 36, d: 3 }
```
```python
objA = { 'a': 10, 'b': 20, 'c': 30 }
objB = { 'a': 3, 'c': 6, 'd': 3 }
combine(objA, objB) # Returns { a: 13, b: 20, c: 36, d: 3 }
```
```ruby
objA = { 'a' => 10, 'b' => 20, 'c' => 30 }
objB = { 'a' => 3, 'c' => 6, 'd' => 3 }
combine(objA, objB) # Returns { a => 13, b => 20, c => 36, d => 3 }
```

The combine function should be a good citizen, so should not mutate the input objects.
