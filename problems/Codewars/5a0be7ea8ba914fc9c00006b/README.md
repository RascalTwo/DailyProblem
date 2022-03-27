[_metadata_:generated]: - "true"

# The falling speed of petals

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a0be7ea8ba914fc9c00006b`](https://www.codewars.com/kata/5a0be7ea8ba914fc9c00006b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

When it's spring Japanese cherries blossom, it's called "sakura" and it's admired a lot. The petals start to fall in late April.

Suppose that the falling speed of a petal is 5 centimeters per second (5 cm/s), and it takes 80 seconds for the petal to reach the ground from a certain branch.

Write a function that receives the speed (in cm/s) of a petal as input, and returns the time it takes for that petal to reach the ground **from the same branch**.

Notes:
* The movement of the petal is quite complicated, so in this case we can see the velocity as a constant during its falling.
* Pay attention to the data types.
* If the initial velocity is non-positive, the return value should be `0`
