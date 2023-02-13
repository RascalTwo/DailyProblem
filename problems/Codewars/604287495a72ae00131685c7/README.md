[_metadata_:generated]: - "true"

# Doubleton number

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                                                                                                                                                       |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`604287495a72ae00131685c7`](https://www.codewars.com/kata/604287495a72ae00131685c7) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924063/c_bnvpsm.svg" alt="C#" title="C#" width="50" />](solve.cs)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

We will call a natural number a "doubleton number" if it contains exactly two distinct digits. For example, `23, 35, 100, 12121` are doubleton numbers, and `123` and `9980` are not. 

For a given natural number `n` (from `1` to `1 000 000`), you need to find the next doubleton number. If `n` itself is a doubleton, return the next bigger than `n`.

#### Examples:

```coffeescript
doubleton(120) == 121
doubleton(1234) == 1311
doubleton(10) == 12
```
```crystal
doubleton(120) == 121
doubleton(1234) == 1311
doubleton(10) == 12
```
```javascript
doubleton(120) === 121
doubleton(1234) === 1311
doubleton(10) === 12
```
```python
doubleton(120) == 121
doubleton(1234) == 1311
doubleton(10) == 12
```
```ruby
doubleton(120) == 121
doubleton(1234) == 1311
doubleton(10) == 12
```
```haskell
doubleton   10 == 12
doubleton  120 == 121
doubleton 1234 == 1311
```
```prolog
doubleton(10,   12).
doubleton(120,  121).
doubleton(1234, 1311).
```
```swift
doubleton(120) == 121
doubleton(1234) == 1311
doubleton(10) == 12
```
```rust
doubleton(10)   == 12
doubleton(120)  == 121
doubleton(1234) == 1311
```
```csharp
Doubleton(120) == 121
Doubleton(1234) == 1311
Doubleton(10) == 12
```
```julia
doubleton(120) # returns 121
doubleton(1234) # returns 1311
doubleton(10) # returns 12
```
```vb
Doubleton(120)  'returns 121
Doubleton(1234) 'returns 1311
Doubleton(10)   'returns 12
```

