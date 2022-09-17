[_metadata_:generated]: - "true"

# search in multidimensional array

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52840d2b27e9c932ff0016ae`](https://www.codewars.com/kata/52840d2b27e9c932ff0016ae) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function that gets a sequence and value and returns `true/false` depending on whether the variable exists in a multidimentional sequence.

Example:
```
locate(['a','b',['c','d',['e']]],'e'); // should return true
locate(['a','b',['c','d',['e']]],'a'); // should return true
locate(['a','b',['c','d',['e']]],'f'); // should return false
```
