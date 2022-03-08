[_metadata_:generated]: - "true"

# Least Larger

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5f8341f6d030dc002a69d7e4`](https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

### Task

Given an array of numbers and an index, return either the index of the smallest number that is larger than the element at the given index, or `-1` if there is no such index ( or, where applicable, `Nothing` or a similarly empty value ).

### Notes

Multiple correct answers may be possible. In this case, return any one of them.  
The given index will be inside the given array.  
The given array will, therefore, never be empty.  

### Example

```javascript
leastLarger( [4, 1, 3, 5, 6], 0 )  =>  3
leastLarger( [4, 1, 3, 5, 6], 4 )  => -1
```
```haskell
leastLarger [4, 1, 3, 5, 6] 0  ->  Just 3
leastLarger [4, 1, 3, 5, 6] 4  -> Nothing
```
```c
least_larger({4, 1, 3, 5, 6}, 5, 0) ==  3;
least_larger({4, 1, 3, 5, 6}, 5, 4) == -1;
```
```python
least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
```
```prolog
least_larger( [4, 1, 3, 5, 6], 0, 3 ).
least_larger( [4, 1, 3, 5, 6], 4, -1 ).
```
```ruby
least_larger( [4, 1, 3, 5, 6], 0 )  =  3
least_larger( [4, 1, 3, 5, 6], 4 )  = -1
```
```go
leastLarger( [] int {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( [] int {4, 1, 3, 5, 6}, 4 )  = -1
```
```java
leastLarger( new int [] {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( new int [] {4, 1, 3, 5, 6}, 4 )  = -1
```
```csharp
leastLarger( new int [] {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( new int [] {4, 1, 3, 5, 6}, 4 )  = -1
```
```cobol
      LeastLarger( [4, 1, 3, 5, 6], 1 )  =  4
      LeastLarger( [4, 1, 3, 5, 6], 5 )  = 0
```
```cpp
leastLarger( vector<int> {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( vector<int> {4, 1, 3, 5, 6}, 4 )  = -1
```
```lambdacalc
least-larger :: List Number -> Number -> Option Number
least-larger < 4 1 3 5 6 > 0  .  Some 3
least-larger < 4 1 3 5 6 > 4  .  None

# use numEncoding Scott
# provide the following for input / output:
nil ~ [] :: List a
cons ~ (:) :: a -> List a -> List a
option ~ maybe :: z -> (a -> z) -> Option a -> z
```
