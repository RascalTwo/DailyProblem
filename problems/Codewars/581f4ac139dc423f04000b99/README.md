[_metadata_:generated]: - "true"

# Transpose two strings in an array

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`581f4ac139dc423f04000b99`](https://www.codewars.com/kata/581f4ac139dc423f04000b99) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given an array that contains two strings. Your job is to create a function that will take those two strings and transpose them, so that the strings go from top to bottom instead of left to right.
```javascript
e.g. transposeTwoStrings(['Hello','World']);

should return

H W  
e o  
l r  
l l  
o d
```
A few things to note:

1. There should be one space in between the two characters
2. You don't have to modify the case (i.e. no need to change to upper or lower)
3. If one string is longer than the other, there should be a space where the character would be

