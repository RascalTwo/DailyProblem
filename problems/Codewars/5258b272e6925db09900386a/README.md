[_metadata_:generated]: - "true"

# For the sake of argument

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5258b272e6925db09900386a`](https://www.codewars.com/kata/5258b272e6925db09900386a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function named `numbers`. 
```if:python 
function should return `True` if all the parameters it is passed are of the integer type or float type. Otherwise, the function should return `False`.
``` 

```if:javascript 
function should return True if all parameters are of the Number type.
```

```if:coffeescript
function should return True if all parameters are of the Number type. otherwise return False
```

The function should accept any number of parameters.

Example usage:

```python
numbers(1, 4, 3, 2, 5); # True
numbers(1, "a", 3); # False
numbers(1, 3, None); # False
numbers(1.23, 5.6, 3.2) # True
```

```coffeescript
numbers(1, 4, 3, 2, 5); // true
numbers(1, "a", 3); // false
numbers(1, 3, NaN) // true
```

```javascript
numbers(1, 4, 3, 2, 5); // true
numbers(1, "a", 3); // false
numbers(1, 3, NaN); // true
```
