[_metadata_:generated]: - "true"

# Ho Ho Ho with Functions!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52af1f150fcae8d33d0009bc`](https://www.codewars.com/kata/52af1f150fcae8d33d0009bc) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Santa is learning programming. And what could be the first program, he wants to write? Yes, the "Hello world!" of Christmas: "Ho Ho Ho!". He wants to write a function `ho()`, which should have the following return values:

```javascript
ho(); // should return "Ho!"
ho(ho()); // should return "Ho Ho!"
ho(ho(ho())); // should return "Ho Ho Ho!"
```

Unfortunately he couldn't find any tutorial, which explains, how he could implement that. Can you help him?

Rules:

* each call of `ho()` must add a "Ho" to the string
* the "Ho"'s must be separated by a space
* at the end of the string, there must be an exclamation mark (`!`), without a space
