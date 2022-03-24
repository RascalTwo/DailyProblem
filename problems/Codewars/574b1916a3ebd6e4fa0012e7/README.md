[_metadata_:generated]: - "true"

# They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`574b1916a3ebd6e4fa0012e7`](https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Task

Give you two strings: ```s1``` and ```s2```. If they are opposite, return `true`; otherwise, return `false`. Note: The result should be a boolean value, instead of a string.

The ```opposite``` means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string.  Also take note of the edge case - if both strings are empty then you should return `false`/`False`.
  
## Examples

```javascript
isOpposite("ab","AB") should return true;
isOpposite("aB","Ab") should return true;
isOpposite("aBcd","AbCD") should return true;
isOpposite("AB","Ab") should return false;
isOpposite("","") should return false;
```
```purescript
isOpposite "ab" "AB" -- => true
isOpposite "aB" "Ab" -- => true
isOpposite "aBcd" "AbCD" -- => true
isOpposite "AB" "Ab" -- => false
isOpposite "" "" -- => false
```
