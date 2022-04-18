[_metadata_:generated]: - "true"

# Right in the Centre

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5f5da7a415fbdc0001ae3c69`](https://www.codewars.com/kata/5f5da7a415fbdc0001ae3c69) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Right in the Center

_This is inspired by one of Nick Parlante's exercises on the [CodingBat](https://codingbat.com/java) online code practice tool._

Given a sequence of characters, does `"abc"` appear in the CENTER of the sequence?

The sequence of characters could contain more than one `"abc"`.

To define CENTER, the number of characters in the sequence to the left and right of the "abc" (which is in the middle) must differ by at most one.

If it is in the CENTER, return `True`. Otherwise, return `False`.

Write a function as the solution for this problem. This kata looks simple, but it might not be easy.

## Example

    is_in_middle("AAabcBB")  ->  True
    is_in_middle("AabcBB")   ->  True
    is_in_middle("AabcBBB")  ->  False
