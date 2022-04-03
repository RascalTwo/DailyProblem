[_metadata_:generated]: - "true"

# "this" is an other problem

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`547f1a8d4a437abdf800055c`](https://www.codewars.com/kata/547f1a8d4a437abdf800055c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

After you've solved @**priyankaherur**'s problem ( http://www.codewars.com/kata/this-is-a-problem/javascript ) you may try to solve this other one.

## The problem:

Having created a function `NamedOne` which takes `first` & `last` names as parameters and returns an object with `firstName`, `lastName` and `fullName` ( = `firstName` + a space + `lastName` ) properties which should be all **accessibles**, we discovered that "accessible" also means "mutable".

If, for example, we've got a "NamedOne" like this :
```javascript
var namedOne = new NamedOne("Naomi","Wang")
namedOne.firstName // -> "Naomi"
namedOne.lastName  // -> "Wang"
namedOne.fullName  // -> "Naomi Wang"
```
```coffeescript
namedOne = new NamedOne("Naomi","Wang")
namedOne.firstName # -> "Naomi"
namedOne.lastName  # -> "Wang"
namedOne.fullName  # -> "Naomi Wang"
```
...properties may be **changed** :
```javascript
namedOne.firstName = "John"
namedOne.firstName // -> "John"
namedOne.lastName = "Doe"
namedOne.lastName  // -> "Doe"
```
```coffeescript
namedOne.firstName = "John"
namedOne.firstName # -> "John"
namedOne.lastName = "Doe"
namedOne.lastName  # -> "Doe"
```
...but **all** properties are not **updated** !

```javascript
namedOne.fullName  // -> "Naomi Wang" 
//-- Oh no ! we want fullName == "John Doe" now !
```
```coffeescript
namedOne.fullName  # -> "Naomi Wang" 
#-- Oh no ! we want fullName == "John Doe" now !
```

## Your mission: 

So the purpose of this kata is to create an object with accessible **and** "<u>updatable</u>" (can i say that?) properties.

* If `.firstName` or `.lastName` are changed, then `.fullName` should also be changed
* If `.fullName` is changed, then `.firstName` and `.lastName` should also be changed.

**Note** : "input format" to `.fullName` will be `firstName + space+ lastName`. If given fullName isn't valid then no property is changed.

## Examples:
```javascript
var namedOne = new NamedOne("Naomi","Wang")

namedOne.firstName = "John"
namedOne.lastName = "Doe"
// ...then...
namedOne.fullName // -> "John Doe"

// -- And :
namedOne.fullName = "Bill Smith"
// ...then...
namedOne.firstName // -> "Bill"
namedOne.lastName  // -> "Smith"

// -- But :
namedOne.fullName = "Tom" // -> no : lastName missing
namedOne.fullName = "TomDonnovan" // -> no : no space between first & last names
namedOne.fullName // -> "Bill Smith" (unchanged)
```
```coffeescript
namedOne = new NamedOne("Naomi","Wang")

namedOne.firstName = "John"
namedOne.lastName = "Doe"
# ...then...
namedOne.fullName # -> "John Doe"

# -- And :
namedOne.fullName = "Bill Smith"
# ...then...
namedOne.firstName # -> "Bill"
namedOne.lastName  # -> "Smith"

# -- But :
namedOne.fullName = "Tom" # -> no : lastName missing
namedOne.fullName = "TomDonnovan" # -> no : no space between first & last names
namedOne.fullName # -> "Bill Smith" (unchanged)
```

Can you change our function to create such a `NamedOne` object ?

(<small> **Hint**: in this kata you'll try to **define properties** of an **object**</small> )

