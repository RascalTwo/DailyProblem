[_metadata_:generated]: - "true"

# Semi-Optional

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`521cd52e790405a74800032c`](https://www.codewars.com/kata/521cd52e790405a74800032c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

We have implemented a function wrap(value) that takes a value of arbitrary type and wraps it in a new JavaScript Object or Python Dict setting  the 'value' key on the new Object or Dict to the passed-in value.

So, for example, if we execute the following code:

```python 
wrapper_obj = wrap("my_wrapped_string"); 
 # wrapper_obj should be  {"value":"my_wrapped_string"}
```


We would then expect the following statement to be true:

```python
wrapper_obj["value"] == "my_wrapped_string"
```

Unfortunately, the code is not working as designed. Please fix the code so that it behaves as specified.


