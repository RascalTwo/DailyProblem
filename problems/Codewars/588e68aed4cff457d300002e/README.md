[_metadata_:generated]: - "true"

# Turn the Mars rover to take pictures

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`588e68aed4cff457d300002e`](https://www.codewars.com/kata/588e68aed4cff457d300002e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Mars rover is on an important mission to take pictures of Mars.

In order to take pictures of all directions it needs an algorithm to help it turn to face the correct position.

Mars rover can face 4 different directions, that would be `N`, `S`, `E`, `W`. Every time it needs to turn it will call a command `turn` passing the current position it is facing and the position it wants to face.

For example:

- if it asks `turn N E` the expected result would be `right`
- if it asks `turn N W` the expected result would be `left`

Mars rover can only make one move at a time and it will only request positions that require a single move.

Can you write an algorithm that tells if it should move `left` or `right`?

![mars rover](https://i.imgur.com/OfPgIh5.png)
