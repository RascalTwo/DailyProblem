[_metadata_:generated]: - "true"

# Monotone travel

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54466996990c921f90000d61`](https://www.codewars.com/kata/54466996990c921f90000d61) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Story
Peter lives on a hill, and he always moans about the way to his home. "It's always just up. I never get a rest". But you're pretty sure that at least at one point Peter's altitude doesn't rise, but fall. To get him, you use a nefarious plan: you attach an altimeter to his backpack and you read the data from his way back at the next day.

# Task
You're given a list of compareable elements:
```c
double heights[n]
```
```csharp
heights = new int[0 ... 100]
```
```haskell
Ord a => [a]
```
```javascript
heights = [h1, h2, h3, …, hn]
```
```python
heights = [Integers or Floats]
```
```ruby
heights = [Integers or Floats]
```
```cobol
      heights = [pic s9(2)]
```

Your job is to check whether for any `x` all successors are greater or equal to `x`.

```c
is_monotone(3, {1, 2, 3}) == true
is_monotone(3, {1, 1, 2}) == true
is_monotone(1, {1})       == true
is_monotone(3, {3, 2, 1}) == false
is_monotone(3, {3, 2, 2}) == false
```
```csharp
Kata.IsMonotone(new int[] {1,2,3}) => true
Kata.IsMonotone(new int[] {1,1,2}) => true
Kata.IsMonotone(new int[] {1})     => true
Kata.IsMonotone(new int[] {3,2,1}) => false
Kata.IsMonotone(new int[] {3,2,2}) => false
```
```haskell
isMonotone [1,2,3] == True
isMonotone [1,1,2] == True
isMonotone [1]     == True
isMonotone [3,2,2] == False
```
```javascript
isMonotone([1,2,3]) == true
isMonotone([1,1,2]) == true
isMonotone([1])     == true
isMonotone([3,2,1]) == false
isMonotone([3,2,2]) == false
```
```python
is_monotone([1,2,3]) == True
is_monotone([1,1,2]) == True
is_monotone([1])     == True
is_monotone([3,2,1]) == False
is_monotone([3,2,2]) == False
```
```ruby
is_monotone([1,2,3]) == True
is_monotone([1,1,2]) == True
is_monotone([1])     == True
is_monotone([3,2,1]) == False
is_monotone([3,2,2]) == False
```
```cobol
      IsMonotone([1,2,3]) = 1
      IsMonotone([1,1,2]) = 1
      IsMonotone([1]) = 1
      IsMonotone([3,2,1]) = 0
      IsMonotone([3,2,2]) = 0
```

If the list is empty, Peter has probably removed your altimeter, so we cannot prove him wrong and he's still right:
```c
is_monotone(0, NULL) => true
```
```csharp
Kata.IsMonotone(new int[] {}) => true
```
```haskell
isMonotone []      == True
```
```javascript
isMonotone([])     == True
```
```python
is_monotone([])     == True
```
```ruby
isMonotone([])     == True
```

Such a sequence is also called *monotone* or [*monotonic* sequence](https://en.wikipedia.org/wiki/Monotonic_function), hence the name `isMonotone`.
