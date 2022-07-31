[_metadata_:generated]: - "true"

# Finding length of the sequence

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5566b0dd450172dfc4000005`](https://www.codewars.com/kata/5566b0dd450172dfc4000005) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

As part of this Kata, you need to find the length of the sequence in an array, between the first and the second occurrence of a specified number.

For example, for a given array `arr`

    [0, -3, 7, 4, 0, 3, 7, 9]
    
Finding length between two `7`s like
    
    lengthOfSequence([0, -3, 7, 4, 0, 3, 7, 9], 7)
    
would return `5`.

For sake of simplicity, there will only be numbers (positive or negative) in the supplied array.

If there are less or more than two occurrences of the number to search for, return `0`, or in Haskell, `Nothing`.
