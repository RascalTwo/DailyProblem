[_metadata_:generated]: - "true"

# Are there any arrows left?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`559f860f8c0d6c7784000119`](https://www.codewars.com/kata/559f860f8c0d6c7784000119) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

<h1>Check your arrows</h1>
You have a quiver of arrows, but some have been damaged. The quiver contains arrows with an optional range information (different types of targets are positioned at different ranges), so each item is an arrow.

You need to verify that you have some good ones left, in order to prepare for battle:
```javascript
anyArrows([{range: 5}, {range: 10, damaged: true}, {damaged: true}])
```
```python
anyArrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])
```
```ruby
anyArrows([{range=> 5}, {range=> 10, damaged=> true}, {damaged=> true}])
```
```elixir
any_arrows?([%{"range" => 5}, %{"range" => 10, "damaged" => true}, %{"damaged" => true}])
```

If an arrow in the quiver does not have a damaged status, it means it's new.

The expected result is a boolean, indicating whether you have any good arrows left.

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
