[_metadata_:generated]: - "true"

# first character that repeats

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54f9f4d7c41722304e000bbb`](https://www.codewars.com/kata/54f9f4d7c41722304e000bbb) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Find the first character that repeats in a String and return that character. 

```javascript
firstDup('tweet') => 't'
firstDup('like') => undefined
```
```python
first_dup('tweet') => 't'
first_dup('like') => None
```
```haskell
firstDup "tweet"         `shouldBe` Just 't'
firstDup (repeat ())     `shouldBe` Just ()
firstDup []              `shouldBe` Nothing
firstDup [1..10]         `shouldBe` Nothing
firstDup [2,46,3,1,1,2]  `shouldBe` 2
```
```ruby
first_dup('tweet') => 't'
first_dup('like') => nil
```

*This is not the same as finding the character that repeats first.*
*In that case, an input of 'tweet' would yield 'e'.*

Another example:

In `'translator'` you should return `'t'`, not `'a'`.
```
v      v  
translator
  ^   ^
```
While second `'a'` appears before second `'t'`, the first `'t'` is before the first `'a'`.
