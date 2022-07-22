[_metadata_:generated]: - "true"

# Array Mappings

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56e20642ddeb0f4fac000344`](https://www.codewars.com/kata/56e20642ddeb0f4fac000344) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Array Mappings

Oh no, the ```map``` method for arrays has been disabled.  Can you fix it?

In case you haven't come across the ```map``` method for arrays, here is how it works:

```javascript
[1,2,3].map(x => x ** 2) === [1,4,9]
[1,2,3].map(x => 2 * x) === [2,4,6]
[1,2,3].map(x => 2 ** x) === [2,4,8]
[1,2,3].map(x => x.toString()) === ["1","2","3"]
["1","2","3"].map(x => parseInt(x)) === [1,2,3]
["random","array","to","be","mapped"].map(x => mapping(x)) === [mapping("random"),mapping("array"),mapping("to"),mapping("be"),mapping("mapped")]
```

The ```map``` method does not mutate the original array.
