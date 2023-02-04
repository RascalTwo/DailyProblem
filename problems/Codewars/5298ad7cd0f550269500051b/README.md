[_metadata_:generated]: - "true"

# Ziiiiip!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5298ad7cd0f550269500051b`](https://www.codewars.com/kata/5298ad7cd0f550269500051b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Let's implement the zipObject function that enables such results

```javascript
zipObject(['fred', 'barney'], [30, 40])
=> { 'fred': 30, 'barney': 40 }

zipObject([['fred', 30], ['barney', 40]])
=> { 'fred': 30, 'barney': 40 }

```

The zipObject creates an object composed from arrays of keys and values. 
It is provided with either a single two dimensional array, i.e. [[key1, value1], [key2, value2]] or with two arrays, one of keys and one of corresponding values.

If only keys are given, then set the values to undefined. 
```javascript
zipObject(['fred', 'barney'])
{ fred: undefined, barney: undefined }
```

If neither keys nor values are specified, then return {}
```javascript
zipObject()
{}
```


