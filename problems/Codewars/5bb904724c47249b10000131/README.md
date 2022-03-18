[_metadata_:generated]: - "true"

# Total amount of points

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5bb904724c47249b10000131`](https://www.codewars.com/kata/5bb904724c47249b10000131) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Our football team finished the championship.
The result of each match look like "x:y". Results of all matches are recorded in the collection.

For example:
```["3:1", "2:2", "0:1", ...]```

Write a function that takes such collection and counts the points of our team in the championship.
Rules for counting points for each match:
- if x > y: 3 points
- if x < y: 0 point
- if x = y: 1 point

Notes:
- there are 10 matches in the championship
- 0 <= x <= 4
- 0 <= y <= 4
