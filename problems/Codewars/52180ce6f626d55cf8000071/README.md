[_metadata_:generated]: - "true"

# Turn String Input into Hash

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52180ce6f626d55cf8000071`](https://www.codewars.com/kata/52180ce6f626d55cf8000071) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Please write a function that will take a string as input and return a hash. The string will be formatted as such. The key will always be a symbol and the value will always be an integer.

```ruby
"a=1, b=2, c=3, d=4"
```
```javascript
"a=1, b=2, c=3, d=4"
```
```python
"a=1, b=2, c=3, d=4"
```

This string should return a hash that looks like
```ruby
{ :a => 1, :b => 2, :c => 3, :d => 4}
```
```javascript
{ 'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
```python
{ 'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
