[_metadata_:generated]: - "true"

# Most Frequent Weekdays

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56eb16655250549e4b0013f4`](https://www.codewars.com/kata/56eb16655250549e4b0013f4) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. `['Monday', 'Tuesday']`, `['Saturday', 'Sunday']`, `['Monday', 'Sunday']`). Week starts with Monday.

__Input:__ Year as an __int__.

__Output:__ The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

__Preconditions:__

* Week starts on Monday.
* Year is between 1583 and 4000. 
* Calendar is Gregorian.

### Examples (input -> output):

```
* 2427 -> ['Friday']
* 2185 -> ['Saturday']
* 2860 -> ['Thursday', 'Friday']
```
