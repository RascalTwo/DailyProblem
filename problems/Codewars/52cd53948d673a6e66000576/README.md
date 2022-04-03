[_metadata_:generated]: - "true"

# Breaking search bad

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52cd53948d673a6e66000576`](https://www.codewars.com/kata/52cd53948d673a6e66000576) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The function must return the sequence of titles that match the string passed as an argument. 

```if:javascript
TITLES is a preloaded sequence of strings. 
```

```javascript
TITLES = ['Rocky 1', 'Rocky 2', 'My Little Poney']
search('ock') --> ['Rocky 1', 'Rocky 2']
```

```python
titles = ['Rocky 1', 'Rocky 2', 'My Little Poney']
search(titles, 'ock') --> ['Rocky 1', 'Rocky 2']
```

But the function return some weird result and skip some of the matching results.

Does the function have special movie taste? 

Let's figure out !
