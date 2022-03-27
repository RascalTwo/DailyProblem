[_metadata_:generated]: - "true"

# For Twins: 2. Math operations

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59c287b16bddd291c700009a`](https://www.codewars.com/kata/59c287b16bddd291c700009a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

### Task:

A magician in the subway showed you a trick, he put an ice brick in a bottle to impress you. The brick's length and width are equal, forming a square; its height may be different. Just for fun and also to impress the magician and people around, you decided to calculate the brick's volume. Write a function `iceBrickVolume` that will accept these parameters:

- `radius` - bottle's radius (always > 0);
- `bottleLength` - total bottle length (always > 0);
- `rimLength` - length from bottle top to brick (always < `bottleLength`);

And return volume of ice brick that magician managed to put into a bottle.

![illustration](https://i.imgur.com/vU2zzm4.png)

### Note:

All inputs are integers. Assume no irregularities to the cuboid brick.
You may assume the bottle is shaped like a cylinder. The brick cannot fit inside the rim. The ice brick placed into the bottle is the largest possible cuboid that could actually fit inside the inner volume. 

### Example 1:
```c
radius = 1
bottle_length = 10
rim_length = 2

volume = 16
```
### Example 2:
```c
radius = 5
bottle_length = 30
rim_length = 7

volume = 1150
```

