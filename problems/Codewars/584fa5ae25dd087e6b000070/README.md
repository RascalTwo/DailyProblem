[_metadata_:generated]: - "true"

# Is my string repeating the same character over and over ?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`584fa5ae25dd087e6b000070`](https://www.codewars.com/kata/584fa5ae25dd087e6b000070) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Your task is very simple:  
Write a function `hasOneChar` returning:  
- `true` if the given string contains the same character repeated all along the string
- `false` otherwise.  

For instance:
```javascript
hasOneChar('aaaaa'); //true
hasOneChar('aaaab'); //false
hasOneChar('bbbbb'); //true
hasOneChar('bbabb'); //false
```

Of course, what comes in mind first is a loop. But the purpose of this Kata is to test your creativity.  
You have to achieve it without using any loops.  

Corner cases: the function `hasOneChar` should return `true` if the string contains one single character.  


Be creative!
