[_metadata_:generated]: - "true"

# Array intersect all

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52a4e42ce950ed50da000748`](https://www.codewars.com/kata/52a4e42ce950ed50da000748) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

**Instructions**

Write a function `intersect` that takes any number of arguments. The function must return an array containing all the values that is present in **every** argument given to the function.

  - All arguments given will be arrays.
  - The first argument determines the order of the returned values.
  - Return an empty array for empty result set.

**Example**
```javascript
var a = ['dog', 'bar', 'foo'];
var b = ['foo', 'bar', 'cat'];
var c = ['gin', 'bar', 'foo'];

intersect(a, b, c); // ['bar', 'foo']
```
```csharp
var a = new string [] { "dog", "bar", "foo" };
var b = new string [] { "foo", "bar", "cat" };
var c = new string [] { "gin", "foo", "bar" };

Kata.Intersect(a, b, c); // { "bar", "foo" }
```
