[_metadata_:generated]: - "true"

# Haskell List Comprehension (ii)

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`53c8bcb1689f84238c000661`](https://www.codewars.com/kata/53c8bcb1689f84238c000661) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

This is the second part. You should do the [previous part][previous] first.
 [previous]: http://www.codewars.com/kata/53c8b29750fe70e4a2000610

Haskell List Comprehension can generate lists by applying filters and transformations.

In this kata we are going to do the same in JavaScript.

To do this, copy the solution you gave in the previous kata and modify it so that the `options` object can accept two parameters more:

* `filters[]`: Array of functions. Each function receives an integer and returns a boolean. Only values that pass the filter, belong to the list.
* `transform(value)`: Is a function that takes a value and returns it muted.

For example:

```javascript
//Filter
function isPrime(num) {
  var result = true;
  if (num !== 2) {
    if (num % 2 === 0) {
      result = false;
    } else {
      for (var x=3; result && x<=Math.sqrt(num); x+=2) {
        if (num % x === 0) {
          result = false;
        }
      }
    }
  }  
  return result;
}

//Transform
function arrayWrapper(num) {
  return [num];
}

ArrayComprehension({
  generator: "1..50",
  filters: [isPrime],
  transform: arrayWrapper
}); // returns [[2], [3], [5], [7], [11], [13], [17], [19], [23], [29], [31], [37], [41], [43], [47]]

```
Cool, is'nt it?
