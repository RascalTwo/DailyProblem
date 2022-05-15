[_metadata_:generated]: - "true"

# Cancer cells

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5931614bb2f657c18c0001c3`](https://www.codewars.com/kata/5931614bb2f657c18c0001c3) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Your task is to write a function which cuts cancer cells from the body.

### Cancer cells are divided into two types:


* <span style="color:red">Advance</span> stage,described as letter <span style="color:red">C</span> 
* <span style="color:Tomato">Initial</span>  stage,described as letter <span style="color:Tomato">c</span> 
 
Rest cells are divided as follows:
* <span style="color:PaleGoldenRod">Normal</span>  cell,described as <span style="color:PaleGoldenRod">lowercase</span>  letter 
* <span style="color:orange">Important</span> cell,described as <span style="color:orange">uppercase</span> letter 
 
### Prerequisites:

* <span style="color:orange">Important</span> cell,cannot be cut out.
* <span style="color:red">Advance</span> cancer cell,should be cut out with adjacent cells if it can be done.

Function input is a string (representing a body), remove "cancer" characters (based on the described rules) and return the body cured of those "cancer" characters.


