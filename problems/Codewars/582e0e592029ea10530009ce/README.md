[_metadata_:generated]: - "true"

# Duck Duck Goose

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`582e0e592029ea10530009ce`](https://www.codewars.com/kata/582e0e592029ea10530009ce) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The objective of [Duck, duck, goose](https://en.wikipedia.org/wiki/Duck,_duck,_goose) is to _walk in a circle_, tapping on each player's head until one is chosen.

----

Task:
Given an array of Player objects (an array of associative arrays in PHP) and an index (**1-based**), return the `name` of the chosen Player(`name` is a property of `Player` objects, e.g `Player.name`)

----

Example:

```
duck_duck_goose([a, b, c, d], 1) should return a.name
duck_duck_goose([a, b, c, d], 5) should return a.name
duck_duck_goose([a, b, c, d], 4) should return d.name
```
```php
// PHP only
duck_duck_goose([$a, $b, $c, $d], 1); // => $a["name"]
duck_duck_goose([$a, $b, $c, $d], 5); // => $a["name"]
duck_duck_goose([$a, $b, $c, $d], 4); // => $d["name"]
```
