[_metadata_:generated]: - "true"

# Cat and Mouse - Easy Version

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57ee24e17b45eff6d6000164`](https://www.codewars.com/kata/57ee24e17b45eff6d6000164) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given a string (x) featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'. 

You need to find out if the cat can catch the mouse from it's current position. The cat can jump over three characters. So:

C.....m returns 'Escaped!'  <-- more than three characters between

C...m returns 'Caught!'   <-- as there are three characters between the two, the cat can jump.
