[_metadata_:generated]: - "true"

# Write out expression!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57e2afb6e108c01da000026e`](https://www.codewars.com/kata/57e2afb6e108c01da000026e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Math hasn't always been your best subject, and these programming symbols always trip you up! I mean, does `**` mean _"Times, Times"_ or _"To the power of"_? Luckily, you can create the function to write out the expressions for you!

The operators you'll need to use are:

```
"+"   -->  "Plus"
"-"   -->  "Minus"
"*"   -->  "Times"
"/"   -->  "Divided By"
"**"  -->  "To The Power Of"
"="   -->  "Equals"
"!="  -->  "Does Not Equal"
```

**Notes:**
* the input will always be given as a string, in the following format: `number space operator space number`; for example: `"1 + 3"` or `"2 - 10"`
* the numbers used will be `1` to `10`
* the valid operators and the relevant texts are stored in the preloaded dictionary/hash `OPERATORS`
* **invalid operators will also be tested**, to which you should return `"That's not an operator!"`


### Examples

```
"4 ** 9"  -->  "Four To The Power Of Nine"
"10 - 5"  -->  "Ten Minus Five"
"2 = 2"   -->  "Two Equals Two"
"2 x 3"   -->  "That's not an operator!"
```

Good luck!
