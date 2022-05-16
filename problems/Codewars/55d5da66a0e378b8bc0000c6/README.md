[_metadata_:generated]: - "true"

# Search JSON for any key value pair

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55d5da66a0e378b8bc0000c6`](https://www.codewars.com/kata/55d5da66a0e378b8bc0000c6) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You have a friend who works for a well known animation studio.  He has heard you talk about your mad programming skills and ask for your help in writing a function that can search some JSON records and return matching character details.  

He needs to be able to search for objects in the collection by any of the objects keys and return an array of all the matches.
  
The basic structure of the JSON object is shown below:

```javascript
let characters = {"characters": [
    {"name":"Bill Cipher", "age":"Unknown", "speciality":"warp reality"},
    // ......
]};
```

The JSON object is preloaded and can be accessed using the variable characters.

Your function will also need to accommodate the following:

- Passed value does not match any keys: in this instance return an empty array.
- Passed key does not exist: in this instance return an empty array.
- Passed val should not be case sensitive.



