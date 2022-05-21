[_metadata_:generated]: - "true"

# The Span Function

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54f2f335cb9d99e8530008d7`](https://www.codewars.com/kata/54f2f335cb9d99e8530008d7) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The span function is a good one to know. It accepts an array and a predicate function and returns two arrays. The first array contains all the elements of the argument array up to the item that caused the first failure of the predicate. The second returned array contains the rest of the original array. The original array is not modified.

For example,

```javascript

function isEven (x) {
  return Math.abs(x) % 2 === 0;
}

var arr = [2,4,6,1,8,10];

// This is true
span(arr, isEven) === [[2,4,6],[1,8,10]]
```

Your task is to...wait for it... write your own span function!!!

Hint/Challenge: If you have completed [the takeWhile function](http://www.codewars.com/kata/the-takewhile-function) and [the dropWhile function](http://www.codewars.com/kata/the-dropwhile-function), then you can solve this problem in one line!
