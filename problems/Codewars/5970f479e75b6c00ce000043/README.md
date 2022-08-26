[_metadata_:generated]: - "true"

# How can I throw an error here?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5970f479e75b6c00ce000043`](https://www.codewars.com/kata/5970f479e75b6c00ce000043) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Try to write a function named `bang` throwing an error with a message string `"Just throw like this!"` with these limits:

+ no invoking `require` function
+ no invoking function constructors
+ no invoking `eval` function
+ no `throw` in your code
+ no `Error` in your code
+ no `\` in your code

Also, we removed `fs`, `assert` and `vm` from global scope, and removed `assert` from `console`.
Do not modify `Error` in global scope, we do not use it to check.
