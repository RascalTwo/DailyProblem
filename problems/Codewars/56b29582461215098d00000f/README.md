[_metadata_:generated]: - "true"

# Lario and Muigi Pipe Problem

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56b29582461215098d00000f`](https://www.codewars.com/kata/56b29582461215098d00000f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

### Issue

Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

The `pipes` connecting your level's stages together need to be fixed before you receive any more complaints.

Pipes list is correct when each `pipe` after the first index is greater (+1) than the previous one, and that there is no duplicates. 

### Task

Given the a list of `numbers`, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included). 
  
### Example

`Input:  1,3,5,6,7,8`
`Output: 1,2,3,4,5,6,7,8`
