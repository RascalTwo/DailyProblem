[_metadata_:generated]: - "true"

# Dot Calculator

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`6071ef9cbe6ec400228d9531`](https://www.codewars.com/kata/6071ef9cbe6ec400228d9531) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Dot Calculator

You have to write a calculator that receives strings for input.
The dots will represent the number in the equation.
There will be dots on one side, an operator, and dots again after the operator.
The dots and the operator will be separated by one space.

Here are the following valid operators :

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `//` Integer Division


## Your Work (Task)

You'll have to return a string that contains dots, as many the equation returns.
If the result is 0, return the empty string.
When it comes to subtraction, the first number will always be greater than or equal to the second number.

### Examples (Input => Output)

```
* "..... + ..............." => "...................."
* "..... - ..."             => ".."
* "..... - ."               => "...."
* "..... * ..."             => "..............."
* "..... * .."              => ".........."
* "..... // .."             => ".."
* "..... // ."              => "....."
* ". // .."                 => ""
* ".. - .."                 => ""
```


