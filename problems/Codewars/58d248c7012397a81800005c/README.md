[_metadata_:generated]: - "true"

# Find out whether the shape is a cube

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`58d248c7012397a81800005c`](https://www.codewars.com/kata/58d248c7012397a81800005c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

To find the volume (centimeters cubed) of a cuboid you use the formula:

```volume = Length * Width * Height```
    
But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!

It's up to you to find out whether the cuboid has equal sides (= is a cube).

Return `true` if the cuboid could have equal sides, return `false` otherwise.

Return `false` for invalid numbers too (e.g volume or side is less than or equal to 0).

Note: the sides must be **integers**
