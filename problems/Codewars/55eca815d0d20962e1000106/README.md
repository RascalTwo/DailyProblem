[_metadata_:generated]: - "true"

# Generate range of integers

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55eca815d0d20962e1000106`](https://www.codewars.com/kata/55eca815d0d20962e1000106) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Implement a function named generateRange(min, max, step), which takes three arguments and generates a range of integers from min to max, with the step. The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)

### Task
Implement a function named

```rust
generateRange(2, 10, 2) // should return iterator of [2,4,6,8,10]
generateRange(1, 10, 3) // should return iterator of [1,4,7,10]
```
```javascript
generateRange(2, 10, 2) // should return array of [2,4,6,8,10]
generateRange(1, 10, 3) // should return array of [1,4,7,10]
```
```elixir
generate_range(2, 10, 2) # should return array of [2,4,6,8,10]
generate_range(1, 10, 3) # should return array of [1,4,7,10]
```
```csharp
GenerateRange(2, 10, 2) == new int[]{ 2, 4, 6, 8, 10 }
GenerateRange(1, 10, 3) == new int[]{ 1, 4, 7, 10 }
```
```racket
(generate-range 2 10 2) ; '(2 4 6 8 10)
(generate-range 1 10 3) ; '(1 4 7 10)
```
```c
generate_range(2, 10, 2, *n) # returns {2, 4, 6, 8, 10}, sets n to 5
generate_range(1, 10, 3, *n) # returns    {1, 4, 7, 10}, sets n to 4
```
```ruby
generate_range(2, 10, 2) # should return array of [2,4,6,8,10]
generate_range(1, 10, 3) # should return array of [1,4,7,10]
```
```python
generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
generate_range(1, 10, 3) # should return list of [1,4,7,10]
```
```nim
generateRange(2, 10, 2) # should return seq of @[2, 4, 6, 8, 10]
generateRange(1, 10, 3) # should return seq of @[1, 4, 7, 10]
```
```julia
generaterange(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
generaterange(1, 10, 3) # should return array of [1, 4, 7, 10]
```
```nasm
generate_range(2, 10, 2, *n) ; returns [2, 4, 6, 8, 10], sets n to 5
generate_range(1, 10, 3, *n) ; returns    [1, 4, 7, 10], sets n to 4
```

### Note
- min < max
- step > 0
- the range does not HAVE to include max (depending on the step)


