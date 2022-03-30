[_metadata_:generated]: - "true"

# Find the divisors! 

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`544aed4c4a30184e960010f4`](https://www.codewars.com/kata/544aed4c4a30184e960010f4) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Create a function named `divisors`/`Divisors` that takes an integer `n > 1` and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (`null` in C#) (use `Either String a` in Haskell and `Result<Vec<u32>, String>` in Rust).

#### Example:

```c
divisors(12); // results in {2, 3, 4, 6}
divisors(25); // results in {5}
divisors(13); // results in NULL
```
```javascript
divisors(12); // should return [2,3,4,6]
divisors(25); // should return [5]
divisors(13); // should return "13 is prime"
```
```elixir
divisors(12) # should return [2,3,4,6]
divisors(25) # should return [5]
divisors(13) # should return "13 is prime"
```
```coffeescript
divisors(12); # should return [2,3,4,6]
divisors(25); # should return [5]
divisors(13); # should return "13 is prime"
```
```haskell
divisors 12   -- should return Right [2,3,4,6]
divisors 25   -- should return Right [5]
divisors 13   -- should return Left "13 is prime"
```
```python
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
```
```ruby
divisors(12) # should return [2,3,4,6]
divisors(25) # should return [5]
divisors(13) # should return "13 is prime"
```
```rust
divisors(12); // should return Ok(vec![2,3,4,6])
divisors(25); // should return Ok(vec![5])
divisors(13); // should return Err("13 is prime")
```
```csharp
Kata.Divisors(12) => new int[] {2, 3, 4, 6};
Kata.Divisors(25) => new int[] {5};
Kata.Divisors(13) => null;
```
```php
divisors(12); // => [2, 3, 4, 6]
divisors(25); // => [5]
divisors(13); // => '13 is prime'
```
