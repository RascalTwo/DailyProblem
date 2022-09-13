[_metadata_:generated]: - "true"

# Ce*s*r*d Strings

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5ff6060ed14f4100106d8e6f`](https://www.codewars.com/kata/5ff6060ed14f4100106d8e6f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

My PC got infected by a strange virus. It only infects my text files and replaces random letters by `*`, `li*e th*s` `(like this)`.

Fortunately, I discovered that the virus hides my censored letters inside root directory.

It will be very tedious to recover all these files manually, so your goal is to implement `uncensor` function that does the hard work automatically.

### Examples

```
uncensor("*h*s *s v*ry *tr*ng*", "Tiiesae") ➜ "This is very strange"

uncensor("A**Z*N*", "MAIG") ➜ "AMAZING"

uncensor("xyz", "") ➜ "xyz"
```


### Notes
  - Expect all discovered letters to be given in the correct order.
  - Discovered letters will match the number of censored ones.
  - Any character can be censored.
