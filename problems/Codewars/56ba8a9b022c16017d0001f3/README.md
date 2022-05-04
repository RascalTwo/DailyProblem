[_metadata_:generated]: - "true"

# Sequence generator

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56ba8a9b022c16017d0001f3`](https://www.codewars.com/kata/56ba8a9b022c16017d0001f3) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Implement function `sequence`, which returns new `n`-size Array filled according to `pattern`.

`pattern` may be:

* a `function` that takes two: `(element, index)`, one: `(element)` or any arguments (similar to `map` function), then filled running this function, in other words: **function describes sequence**,
* number, string or any other object, then filled by copying, this object `n`-times.

**Examples:**
```javascript
sequence(3, 4); // [4, 4, 4]
sequence(5, []); // [[], [], [], [], []]
sequence(2, "s"); // ["s", "s"]
sequence(5, (x, idx) => idx%2) // [0, 1, 0, 1, 0];
sequence(10, (x, idx) => idx+1) // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
*Note:* Sequences are great to work with functional methods like `map`, `reduce`, `forEach`, `every` or `any`. For example:
```javascript
// sum of numbers 1-10
let sum = sequence(10, (x, idx) => idx+1).reduce((sum, num) => sum + num);
```
Be careful with long sequences. They are just arrays, every element is created when function is called.

For [lazy sequences](https://en.wikipedia.org/wiki/Lazy_evaluation) (elements created when needed) use [Iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).


