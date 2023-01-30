[_metadata_:generated]: - "true"

# Thinkful - Object Drills: Vectors

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`587f1e1f39d444cee6000ad4`](https://www.codewars.com/kata/587f1e1f39d444cee6000ad4) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Create a `Vector` class with `x` and a `y` attributes that represent component magnitudes in the x and y directions.

Your vectors should handle vector additon with an `.add()` method that takes a second vector as an argument and returns a new vector equal to the sum of the vector you call `.add()` on and the vector you pass in.

For example:

```python
>>> a = Vector(3, 4)
>>> a.x
3
>>> a.y
4
>>> b = Vector(1, 2)
>>> c = a.add(b)
>>> c.x
4
>>> c.y
6
```

Adding vectors when you have their components is easy: just add the two x components together and the two y components together to get the x and y components for the vector sum.

