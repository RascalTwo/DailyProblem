[_metadata_:generated]: - "true"

# 'x' marks the spot.

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5777fe3f355edbf0a5000d11`](https://www.codewars.com/kata/5777fe3f355edbf0a5000d11) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

#'x' marks the spot

##Task:

Given a two dimensional array, return the co-ordinates of 'x'.

```if:javascript
If 'x' is not inside the array, or if 'x' appears multiple times, return `[]`
```

```if:c
If 'x' is not inside the array, or if 'x' appears multiple times return `{-1, -1}`.
```

The co-ordinates should be zero indexed.

You should assume you will always get an array as input. The array will only contain `'x'`s and `'o'`s.

Example test cases:

```
'Return an empty array if input is an empty array' => []

[] 

'Return an empty array if no x found' => []

[
  ['o', 'o'],
  ['o', 'o']
]

'Return an empty array if more than one x found' => []

[
  ['x', 'o'],
  ['o', 'x']
]

'Return [0,0] when x at top left' => [0, 0]

[
  ['x', 'o'],
  ['o', 'o']
]

'Return [4,6] for the example below' => [4, 6]

[
  ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'o', 'o', 'o', 'x', 'o'],
  ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
]
```
