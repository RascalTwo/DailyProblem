[_metadata_:generated]: - "true"

# JSON.parse Date Reviver

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`533b0d5e7abec41550000a9e`](https://www.codewars.com/kata/533b0d5e7abec41550000a9e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

JSON.stringify is very useful for serializing javascript objects and values into a string. JSON.parse is very useful for deserializing these strings back into the original objects. Unfortunately, the JSON format has no way of representing a Date object. Instead, it creates a string for that object, and includes that in the serialized string instead. The problem is, when JSON.parse deserializes the JSON string, it sees it as a simple string, and does not convert it into a real Date object.

Let's fix that with a `JSON_Date_reviver` function for use with JSON.parse. JSON.parse allows for a second, optional parameter; a function that can take two arguments, known as the "reviver". The first is the "key" of the property in an object; the second is the "value" of that property. If the parser is not going over an object's property, the "key" is empty, and the value is whatever value it is currently trying to parse. Whatever value is returned by the function will be used as the value slotted into the parsed object at the end.

Your job is to write the `JSON_Date_reviver()` function to return a real Date object when the value passed in is one of those date strings. If it is not a "date string", however, the original value should be returned as-is.

For reference, here are some example "date strings":
```javascript
"2014-04-01T18:51:35.275Z"
"1994-10-03T07:48:15.704Z"
"1986-12-24T03:49:25.419Z"
"+198456-09-18T00:02:27.626Z"
"-260424-08-20T15:37:04.134Z"
"+080521-01-20T03:54:16.348Z"
```
