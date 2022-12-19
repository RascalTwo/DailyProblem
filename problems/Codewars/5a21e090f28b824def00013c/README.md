[_metadata_:generated]: - "true"

# Swap items in a dictionary

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a21e090f28b824def00013c`](https://www.codewars.com/kata/5a21e090f28b824def00013c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

```if:python
In this kata, you will take the keys and values of a `dict` and swap them around.
```
```if:javascript
In this kata, you will take the keys and values of an `object` and swap them around.
```
```if:haskell
In this kata, you will take the keys and values of a `Map` and swap them around.
```

You will be given a dictionary, and then you will want to return a dictionary with the old values as the keys, and list the old keys as values under their original keys.

For example, given the dictionary: ```{'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}```,

you should return: ```{'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}```


# Notes:

* The dictionary given will only contain strings
* The dictionary given will not be empty
* You do not have to sort the items in the lists
