[_metadata_:generated]: - "true"

# Naughty or Nice

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5662b14e0a1fb8320a00005c`](https://www.codewars.com/kata/5662b14e0a1fb8320a00005c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Santa is coming to town and he needs your help finding out who's been naughty or nice. You will be given an entire year of JSON data following this format:

```javascript
{
    January: {
        '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
    },
    February: {
        '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
    },
    ...
    December: {
        '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
    }
}
```
Your function should return `"Naughty!"` or `"Nice!"` depending on the total number of occurrences in a given year (whichever one is greater). If both are equal, return `"Nice!"`
