[_metadata_:generated]: - "true"

# Meeting

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59df2f8f08c6cec835000012`](https://www.codewars.com/kata/59df2f8f08c6cec835000012) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

John has invited some friends. His list is:
```
s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
```

Could you make a program that 
- makes this string uppercase
- gives it sorted in alphabetical order by last name. 

When the last names are the same, sort them by first name.
Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function `meeting(s)` will be:
```
"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
```
It can happen that in two distinct families with the same family name two people have the same first name too.

#### Notes
- You can see another examples in the "Sample tests".


