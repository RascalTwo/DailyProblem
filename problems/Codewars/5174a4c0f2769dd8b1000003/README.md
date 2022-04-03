[_metadata_:generated]: - "true"

# Sort Numbers

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5174a4c0f2769dd8b1000003`](https://www.codewars.com/kata/5174a4c0f2769dd8b1000003) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

```r
solution(c(1, 2, 3, 10, 5)) # should return c(1, 2, 3, 5, 10)
solution(NULL)              # should return NULL
```

```php
solution([1, 2, 10, 50, 5]); // should return [1,2,5,10,50]
solution(null); // should return []
```

```javascript
solution([1, 2, 10, 50, 5]); // should return [1,2,5,10,50]
solution(null); // should return []
```

```typescript
solution([1, 2, 10, 50, 5]); // should return [1, 2, 5, 10, 50]
solution([]); // should return []
```

```coffeescript
solution([1, 2, 10, 50, 5]) # should return [1,2,5,10,50]
solution(null) # should return []
```

```ruby
solution([1, 2, 10, 50, 5]) # should return [1,2,5,10,50]
solution(nil) # should return []
```

```python
solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
```

```julia
solution([1, 2, 10, 50, 5]) # should return [1,2,5,10,50]
solution(nothing) # should return []
```

```csharp
SortNumbers(new int[] { 1, 2, 10, 50, 5 }); // should return new int[] { 1, 2, 5, 10, 50 }
SortNumbers(null); // should return new int[] { }
```

```rust
sort_numbers(&vec![1, 2, 3, 10, 5]); // should return vec![1, 2, 3, 5, 10]
sort_numbers(&vec![]); // should return !vec[]
```

```haskell
sortNumbers [1, 2, 10, 50, 5] = Just [1, 2, 5, 10, 50]
sortNumbers [] = Nothing
```

```lambdacalc
# (Note in Lambda Calculus we have lists instead of arrays.)
nums = cons 1 (cons 2 (cons 10 (cons 50 (cons 5 nil))))
sort nums # cons 1 (cons 2 (cons 5 (cons 10 (cons 50 nil))))
```

```cpp
sortNumbers({1, 2, 10, 50, 5}) // sholud return {1, 2, 5, 10, 50}
sortNumbers({}) // should return {}
```

```c
int array[5] = {1, 2, 10, 50, 5};
sort_ascending(5, array); // array is now {1, 2, 5, 10, 50}
sort_ascending(0, NULL); // nothing to do for empty array
```

```cobol
      SortNumbers([1, 2, 10, 50, 5])
      *  -> res = [1, 2, 5, 10, 50]
      SortNumbers([])
      *  -> res = []
```

~~~if:lambdacalc
## Lambda Calculus

- Purity: LetRec
- Num encoding: BinaryScott
- For LC, there won't be `null` inputs.
- Instead of arrays, we have cons lists. Define the following, which the tests will use to construct inputs and test outputs:
  - `nil : List a` (empty list)
  - `cons : a -> List a -> List a` (add to head)
  - `foldr : (a -> b -> b) -> b -> List a -> b` (right-associative fold / reduce)

### Optional Performance Check

By default the tests are lenient with respect to performance. If you would like to demonstrate that your solution is fast, you can opt in to a stricter test suite (more lists, longer lists, higher numbers). Just change `perf-tests = Low` to `perf-tests = High`.
~~~

