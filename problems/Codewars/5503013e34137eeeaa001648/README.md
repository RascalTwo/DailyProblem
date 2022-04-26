[_metadata_:generated]: - "true"

# Give me a Diamond

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5503013e34137eeeaa001648`](https://www.codewars.com/kata/5503013e34137eeeaa001648) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

## Task

You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (`*`) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (`\n`).

Return `null/nil/None/...` if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.


## Examples

A size 3 diamond:

```
 *
***
 *
```

...which would appear as a string of `" *\n***\n *\n"`


A size 5 diamond:

```
  *
 ***
*****
 ***
  *
```

...that is: 
```
"  *\n ***\n*****\n ***\n  *\n"
```

