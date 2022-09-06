[_metadata_:generated]: - "true"

# letters only, please!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59be6bdc4f98a8a9c700007d`](https://www.codewars.com/kata/59be6bdc4f98a8a9c700007d) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Let's assume we need "clean" strings. Clean means a string should only contain letters `a-z`, `A-Z` and spaces. We assume that there are no double spaces or line breaks.

Write a function that takes a string and returns a string without the unnecessary characters.


### Examples

```python
remove_chars('.tree1')    ==> 'tree'

remove_chars("that's a pie$ce o_f p#ie!")  ==> 'thats a piece of pie'

remove_chars('john.dope@dopington.com')    ==> 'johndopedopingtoncom'

remove_chars('my_list = ["a","b","c"]')    ==> 'mylist  abc'

remove_chars('1 + 1 = 2')    ==> '    ' (string with 4 spaces)

remove_chars("0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_")  ==> '' (empty string)
```

```javascript
removeChars('.tree1')    ==> 'tree'

removeChars("that's a pie$ce o_f p#ie!")  ==> 'thats a piece of pie'

removeChars('john.dope@dopington.com')    ==> 'johndopedopingtoncom'

removeChars('my_list = ["a","b","c"]')    ==> 'mylist  abc'

removeChars('1 + 1 = 2')    ==> '    ' (string with 4 spaces)

removeChars("0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_")  ==> '' (empty string)
```
