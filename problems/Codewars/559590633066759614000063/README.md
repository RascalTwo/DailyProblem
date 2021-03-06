[_metadata_:generated]: - "true"

# The highest profit wins!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                                                                                                                                                                |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`559590633066759614000063`](https://www.codewars.com/kata/559590633066759614000063) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/java_un8ru7.svg" alt="Java" title="Java" width="50" />](class.java)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

### Story

Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

### Task

Write a function that returns both the minimum and maximum number of the given list/array. 

### Examples

```haskell
minMax [1,2,3,4,5] `shouldBe` (1, 5)
minMax [2334454,5] `shouldBe` (5, 2334454)
minMax [1]         `shouldBe` (1, 1)
```
```javascript
minMax([1,2,3,4,5])   == [1,5]
minMax([2334454,5])   == [5, 2334454]
minMax([1])           == [1, 1]
```
```coffeescript
minMax [1..5]      == [1, 5]
minMax [2334454,5] == [5, 2334454]
minMax [1]         == [1, 1]
```
```python
min_max([1,2,3,4,5])   == [1,5]
min_max([2334454,5])   == [5, 2334454]
min_max([1])           == [1, 1]
```
```ruby
min_max([1,2,3,4,5])   == [1,5]
min_max([2334454,5])   == [5, 2334454]
min_max([1])           == [1, 1]
```
```java
MinMax.minMax(new int[]{1,2,3,4,5}) == {1,5}
MinMax.minMax(new int[]{2334454,5}) == {5, 2334454}
MinMax.minMax(new int[]{1}) == {1, 1}
```
```csharp
MinMax.minMax(new int[]{1,2,3,4,5}) == {1,5}
MinMax.minMax(new int[]{2334454,5}) == {5, 2334454}
MinMax.minMax(new int[]{1}) == {1, 1}
```
```c
// In C assign to the 'min' and 'max' pointers
min_max(int[]{1,2,3,4,5}) // min = 1, max = 5
min_max(int[]{2334454,5}) // min = 5, max = 2334454
min_max(int[]{1})         // min = 1, max = 1
```

### Remarks
All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for `null`, `undefined` or similar.
