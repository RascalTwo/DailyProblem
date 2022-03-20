[_metadata_:generated]: - "true"

# Count by X

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5513795bd3fafb56c200049e`](https://www.codewars.com/kata/5513795bd3fafb56c200049e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Create a function with two arguments that will return an array of the first (n) multiples of (x). 

Assume both the given number and the number of times to count will be positive numbers greater than 0. 

Return the results as an array (or list in Python, Haskell or Elixir).

Examples:
```cpp
countBy(1,10)  should return  {1,2,3,4,5,6,7,8,9,10}
countBy(2,5)  should return {2,4,6,8,10}
```
```javascript
countBy(1,10) === [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) === [2,4,6,8,10]
```
```nasm
mov rdi, .memory ; {,,,,,,,,}
mov esi, 1
mov rdx, 10
call cntbyx     ; [RAX] <- {1,2,3,4,5,6,7,8,9,10}

mov rdi, .memory  ; {,,,,}
mov esi 2
mov rdx, 5
call cntbyx     ; [RAX] <- {2,4,6,8,10}
```
```coffeescript
countBy(1,10) == [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) == [2,4,6,8,10]
```
```dart
countBy(1,10) === [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) === [2,4,6,8,10]
```
```coffeescript
countBy(1,10) == [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) == [2,4,6,8,10]
```
```python
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
```
```ruby
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
```
```crystal
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
```
```haskell
countBy 1 10 `shouldBe` [1,2,3,4,5,6,7,8,9,10]
countBy 2  5 `shouldBe` [2,4,6,8,10]
```
```elixir
count_by(1, 10) == [1,2,3,4,5,6,7,8,9,10]
count_by(2, 5) == [2,4,6,8,10]
```
```solidity
countBy(1,10) // should return [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) // should return [2,4,6,8,10]
```
```php
countBy(1,10) // should return [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) // should return [2,4,6,8,10]
```
```groovy
Kata.countBy(1, 10) == [1,2,3,4,5,6,7,8,9,10]
Kata.countBy(2, 5) == [2,4,6,8,10]
```

```racket
(count-by 1 10) ; returns '(1 2 3 4 5 6 7 8 9 10)
(count-by 2 5)  ; returns '(2 4 6 8 10)
```


