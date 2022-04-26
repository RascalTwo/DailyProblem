[_metadata_:generated]: - "true"

# Limit string length - 1

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5208fc3cb613bc725f000142`](https://www.codewars.com/kata/5208fc3cb613bc725f000142) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The function must return the truncated version of the given string up to the given limit followed by `"..."` if the result is shorter than the original. Return the same string if nothing was truncated. 

Example:

```
solution('Testing String', 3) --> 'Tes...'
solution('Testing String', 8) --> 'Testing ...'
solution('Test', 8)           --> 'Test'
```

