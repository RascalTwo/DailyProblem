[_metadata_:generated]: - "true"

# Anonymous Returns.

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`53d4eec01f1a9b3020000786`](https://www.codewars.com/kata/53d4eec01f1a9b3020000786) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

When a function is called by itself it is bound to the global context; the `this` variable of the function will be bound to the global object.

When the `getNameFunc` function is called on the `alpha` object the value of the `name` variable outside of the object is returned: `"The Window"`. 

We do not want this, we want the value of the `name` property inside the `alpha` object to be returned.

Fix `getNameFunc` so the right value is returned.

For more information: [Binding](http://alistapart.com/article/getoutbindingsituations)
