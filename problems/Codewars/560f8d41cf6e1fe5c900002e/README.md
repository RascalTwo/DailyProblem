[_metadata_:generated]: - "true"

# Find variable which breaks strict comparison!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`560f8d41cf6e1fe5c900002e`](https://www.codewars.com/kata/560f8d41cf6e1fe5c900002e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In JavaScript, there is a special case where strict comparison of the same variable returns false! 
Try to find out what must be done to get such result!

```javascript
var x = something;
x === x // returns false!
```

Write a function which will return value for which strict comparison will give false!
