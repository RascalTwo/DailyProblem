[_metadata_:generated]: - "true"

# Find the Capitals

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`53573877d5493b4d6e00050c`](https://www.codewars.com/kata/53573877d5493b4d6e00050c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Complete the method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings.

The method should return an array of sentences declaring the state or country and its capital.


## Examples

```ruby
state_capitals = [{state: 'Maine', capital: 'Augusta'}]
capital(state_capitals)[0] # returns "The capital of Maine is Augusta"

country_capitals = [{'country' => 'Spain', 'capital' => 'Madrid'}]
capital(country_capitals)[0] # returns "The capital of Spain is Madrid"

mixed_capitals: [{"state" => 'Maine', capital: 'Augusta'}, {country: 'Spain', "capital" => "Madrid"}]
capital(mixed_capitals)[0] # returns "The capital of Maine is Augusta"
```

```javascript
state_capitals = [{state: 'Maine', capital: 'Augusta'}]
capital(state_capitals)[0] // returns "The capital of Maine is Augusta"

country_capitals = [{'country' : 'Spain', 'capital' : 'Madrid'}]
capital(country_capitals)[0]  // returns "The capital of Spain is Madrid"

mixed_capitals: [{"state" : 'Maine', capital: 'Augusta'}, {country: 'Spain', "capital" : "Madrid"}]
capital(mixed_capitals)[1] // returns "The capital of Spain is Madrid"
```

```python
[{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
[{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
[{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]
```

```rust
&[Capital { country: None, state: Some("Maine"), capital: "Augusta" }] -> vec!["The capital of Maine is Augusta".to_string()]
&[Capital { country: Some("Spain"), state: None, capital: "Madrid" }] -> vec!["The capital of Spain is Madrid".to_string()]
&[Capital { country: None, state: Some("Maine"), capital: "Augusta" }, Capital { country: Some("Spain"), state: None, capital: "Madrid" }] -> vec!["The capital of Maine is Augusta".to_string(), "The capital of Spain is Madrid".to_string()]

```
