[_metadata_:generated]: - "true"

# Simple Fun #136: Missing Values

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`58a66c208b88b2de660000c3`](https://www.codewars.com/kata/58a66c208b88b2de660000c3) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Task

 You are given a sequence of positive ints where every element appears `three times`, except one that appears only `once` (let's call it `x`) and one that appears only `twice` (let's call it `y`).

 Your task is to find `x * x * y`.

# Example

 For `arr=[1, 1, 1, 2, 2, 3]`, the result should be `18`
 
 `3 x 3 x 2 = 18`
 
 For `arr=[6, 5, 4, 100, 6, 5, 4, 100, 6, 5, 4, 200]`, the result should be `4000000`
 
 `200 x 200 x 100 = 4000000`

# Input/Output

 - `[input]` integer array `arr`

  an array contains positive integers.

 - `[output]` an integer

 The value of `x * x * y`
