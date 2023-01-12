[_metadata_:generated]: - "true"

# Run your String

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54cb61619b30e88e44001048`](https://www.codewars.com/kata/54cb61619b30e88e44001048) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

1) Function should accept two arguments:

 - arg: any type
 - object with properties: 
 
      - param: string type.
      - func:  string type. This string is a body of executable function

 
2)  Function should evaluate code of string passed as 'func' with parameter arg passed as argument and return result of execution


Example:
```javascript
var arg = 4,                         // arg for "string" function call
    obj = {
      param: 'num',                  // parameter name for function in string  
      func: 'return Math.sqrt(num)'  // function that need call with arg var
    };
    
runYourString(arg, obj)              // we expect it should return 2 which is a result of square root of 4
```

ps: 
Solution of this Kata just fun language trick.

Usage of this code in production is not recommended. 
