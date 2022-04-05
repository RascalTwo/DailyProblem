[_metadata_:generated]: - "true"

# Find the capitals

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`539ee3b6757843632d00026b`](https://www.codewars.com/kata/539ee3b6757843632d00026b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Instructions 

Write a function that takes a single string (`word`) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

# Example

```javascript
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
```
```ruby
Test.assert_equals( capitals('CodEWaRs'), [0,3,4,6] );
```
```haskell
capitals ""         `shouldBe` []
capitals "CodEWaRs" `shouldBe` [0,3,4,6]
capitals "aAbB"     `shouldBe` [1,3]
capitals "4ysdf4"   `shouldBe` []
capitals "ABCDEF"   `shouldBe` [0..5]
```
```csharp
Assert.AreEqual(Kata.Capitals("CodEWaRs"), new int[]{0,3,4,6});
```
