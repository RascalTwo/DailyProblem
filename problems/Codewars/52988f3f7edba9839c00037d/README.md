[_metadata_:generated]: - "true"

# The reject() function

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52988f3f7edba9839c00037d`](https://www.codewars.com/kata/52988f3f7edba9839c00037d) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Implement a function which filters out array values which satisfy the given predicate.

```javascript
reject([1, 2, 3, 4, 5, 6], (n) => n % 2 === 0)  =>  [1, 3, 5]
```
```csharp
Kata.Reject(new int[] {1, 2, 3, 4, 5, 6}, (n) => n % 2 == 0)  =>  new int[] {1, 3, 5}
```
```php
reject([1, 2, 3, 4, 5, 6], function ($n) {return $n % 2 == 0;})  =>  [1, 3, 5]
```
```python
reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)  =>  [1, 3, 5]
```
