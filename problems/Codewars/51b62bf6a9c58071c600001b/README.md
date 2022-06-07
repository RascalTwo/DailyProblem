[_metadata_:generated]: - "true"

# Roman Numerals Encoder

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`51b62bf6a9c58071c600001b`](https://www.codewars.com/kata/51b62bf6a9c58071c600001b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:
```javascript
solution(1000); // should return 'M'
```
```coffeescript
solution(1000) # should return 'M'
```
```ruby
solution(1000) # should return 'M'
```
```python
solution(1000) # should return 'M'
```
```haskell
solution 1000 -- should return "M"
```
```java
conversion.solution(1000); //should return "M"
```
```typescript
solution(1000); // should return 'M'
```
```cpp
solution(1000); // should return "M"
```
```php
solution(1000); // should return "M"
```
```csharp
RomanConvert.Solution(1000) -- should return "M"
```
```swift
solution(1000) // should return "M"
```
```elixir
solution(1000) # should return "M"
```
```r
solution(1000) # should return "M"
```
```c
solution(1000); // => "M"
```
```nim
solution(1000) # should return "M"
```
```lua
romanEncoder(1000) -- should return 'M'
```
```scala
Roman.encode(1000) // should return "M"
```
```kotlin
encode(1000) // should return "M"
```
```clojure
(solution 1000) ;; should return "M"
```
```julia
encoderomannumeral(1000) # should return "M"
```

Help:
```
Symbol	Value
I	      1
V	      5
X	      10
L	      50
C	      100
D	      500
M	      1,000
```

Remember that there can't be more than 3 identical symbols in a row.


More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

