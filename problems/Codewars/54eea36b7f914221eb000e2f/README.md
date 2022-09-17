[_metadata_:generated]: - "true"

# Alphabetize a list by the nth character 

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54eea36b7f914221eb000e2f`](https://www.codewars.com/kata/54eea36b7f914221eb000e2f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n).  The function should alphabetize the list based on the nth letter of each word.

The letters should be compared case-insensitive. If both letters are the same, order them normally (lexicographically), again, case-insensitive.

example:
```javascript 
function sortIt('bid, zag', 2) //=> 'zag, bid'
```
```ruby 
function sortIt('bid, zag', 2) //=> 'zag, bid'
```
```python 
function sortIt('bid, zag', 2) #=> 'zag, bid'
```
```haskell
sortIt ["bid", "zag"] 2 `shouldBe` ["zag", "bid"]
```

The length of all words provided in the list will be >= n.  The format will be "x, x, x". In Haskell you'll get a list of `String`s instead.
