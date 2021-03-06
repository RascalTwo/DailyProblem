[_metadata_:generated]: - "true"

# Add Length

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`559d2284b5bb6799e9000047`](https://www.codewars.com/kata/559d2284b5bb6799e9000047) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

```javascript
addLength('apple ban') => ["apple 5", "ban 3"]
addLength('you will win') => ["you 3", "will 4", "win 3"]
```
```python
add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
```
```ruby
add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
```
```coffeescript
addLength 'apple ban' => ["apple 5", "ban 3"]
addLength 'you will win' => ["you 3", "will 4", "win 3"]
```
```elixir
add_length("apple ban") => ["apple 5", "ban 3"]
add_length("you will win") => ["you 3", "will 4", "win 3"]
```
```csharp
Kata.AddLength("apple ban")    => new string[] {"apple 5", "ban 3"};
Kata.AddLength("you will win") => new string[] {"you 3", "will 4", "win 3"};
```
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

**Note:** String will have at least one element; words will always be separated by a space. 

