[_metadata_:generated]: - "true"

# Take the Derivative

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5963c18ecb97be020b0000a2`](https://www.codewars.com/kata/5963c18ecb97be020b0000a2) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

This function takes two numbers as parameters, the first number being the coefficient, and the second number being the exponent.

Your function should multiply the two numbers, and then subtract 1 from the exponent. Then, it has to print out an expression (like 28x^7). `"^1"` should not be truncated when exponent = 2.


For example:
``` javascript
derive(7, 8)
```
``` haskell
derive 7 8
```
In this case, the function should multiply 7 and 8, and then subtract 1 from 8. It should output `"56x^7"`, the first number 56 being the product of the two numbers, and the second number being the exponent minus 1.

``` javascript
derive(7, 8) --> this should output "56x^7" 
derive(5, 9) --> this should output "45x^8" 
```
``` haskell
derive 7 8 == "56x^7"
derive 5 9 == "45x^8"
```

**Notes:**
* The output of this function should be a string
* The exponent will never be 1, and neither number will ever be 0
