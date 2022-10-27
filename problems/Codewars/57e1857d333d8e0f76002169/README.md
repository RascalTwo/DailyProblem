[_metadata_:generated]: - "true"

# Loose Change!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57e1857d333d8e0f76002169`](https://www.codewars.com/kata/57e1857d333d8e0f76002169) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You've been collecting change all day, and it's starting to pile up in your pocket, but you're too lazy to see how much you've found.

Good thing you can code!

Create ```change_count()``` to return a dollar amount of how much change you have!

Valid types of change include:
```
penny: 0.01
nickel: 0.05
dime: 0.10
quarter: 0.25
dollar: 1.00
```

```if:python
These amounts are already preloaded as floats into the `CHANGE` dictionary for you to use!
```
```if:ruby
These amounts are already preloaded as floats into the `CHANGE` hash for you to use!
```
```if:javascript
These amounts are already preloaded as floats into the `CHANGE` object for you to use!
```
```if:php
These amounts are already preloaded as floats into the `CHANGE` (a constant) associative array for you to use!
```

You should return the total in the format ```$x.xx```.

Examples:

```python
change_count('nickel penny dime dollar') == '$1.16'
change_count('dollar dollar quarter dime dime') == '$2.45'
change_count('penny') == '$0.01'
change_count('dime') == '$0.10'
```
```javascript
changeCount('nickel penny dime dollar') == '$1.16'
changeCount('dollar dollar quarter dime dime') == '$2.45'
changeCount('penny') == '$0.01'
changeCount('dime') == '$0.10'
```
```ruby
changeCount('nickel penny dime dollar') == '$1.16'
changeCount('dollar dollar quarter dime dime') == '$2.45'
changeCount('penny') == '$0.01'
changeCount('dime') == '$0.10'
```
```php
changeCount('nickel penny dime dollar') == '$1.16'
changeCount('dollar dollar quarter dime dime') == '$2.45'
changeCount('penny') == '$0.01'
changeCount('dime') == '$0.10'
```

Warning, some change may amount to over ```$10.00```!
