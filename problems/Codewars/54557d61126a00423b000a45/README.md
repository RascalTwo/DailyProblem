[_metadata_:generated]: - "true"

# shorter concat [reverse longer]

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54557d61126a00423b000a45`](https://www.codewars.com/kata/54557d61126a00423b000a45) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given 2 strings, `a` and `b`, return a string of the form: `shorter+reverse(longer)+shorter.`


In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

Strings `a` and `b` may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).  
If `a` and `b` have the same length treat `a` as the longer producing `b+reverse(a)+b`
