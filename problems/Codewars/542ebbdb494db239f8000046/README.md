[_metadata_:generated]: - "true"

# What's up next?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`542ebbdb494db239f8000046`](https://www.codewars.com/kata/542ebbdb494db239f8000046) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a sequence of items and a specific item in that sequence, return the item immediately following the item specified. If the item occurs more than once in a sequence, return the item after the first occurence. This should work for a sequence of any type.

When the item isn't present or nothing follows it, the function should return nil in Clojure and Elixir, Nothing in Haskell, undefined in JavaScript, None in Python.

```clojure
(next-item (range 1 10000) 7) ;=> 8
(next-item ["Joe" "Bob" "Sally"] "Bob") ;=> "Sally"
```

```haskell
next 7 [1..10000] -- Just 8
next "Bob" ["Joe", "Bob", "Sally"] -- Just "Sally"
```

```javascript
nextItem([1, 2, 3, 4, 5, 6, 7], 3) # 4
nextItem("testing", "t") # "e"
```
```elixir
next_item([1, 2, 3, 4, 5, 6, 7], 3) #=> 4
next_item(["Joe" "Bob" "Sally"], "Bob") #=> "Sally"
```
```rust
next_item([1, 2, 3, 4, 5, 6, 7], 3) //=> 4
next_item(["Joe" "Bob" "Sally"], "Bob") //=> "Sally"
```
```python
next_item([1, 2, 3, 4, 5, 6, 7], 3) # => 4
next_item(['Joe', 'Bob', 'Sally'], 'Bob') # => "Sally"
```

