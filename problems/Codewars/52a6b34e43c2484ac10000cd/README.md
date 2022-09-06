[_metadata_:generated]: - "true"

# Naughty or Nice?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52a6b34e43c2484ac10000cd`](https://www.codewars.com/kata/52a6b34e43c2484ac10000cd) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Happy Holidays fellow Code Warriors!

It's almost Christmas! That means Santa's making his list, and checking it twice. Unfortunately, elves accidentally mixed the Naughty and Nice list together! Santa needs your help to save Christmas!

## Save Christmas!
Santa needs you to write two functions. Both of the functions accept a sequence of objects. The first one returns a sequence containing only the names of the nice people, and the other returns a sequence containing only the names of the naughty people. Return an empty sequence `[]` if the result from either of the functions contains no names.

The objects in the passed will represent people. Each object contains two properties: `name` and `wasNice`.<br/>
`name` - The name of the person<br/>
`wasNice` - True if the person was nice this year, false if they were naughty

## Person Object Examples

```javascript
{ name: 'Warrior reading this kata', wasNice: true }
{ name: 'xDranik', wasNice: false }
```

```if:haskell
In Haskell, a `Warrior` is simply a tuple `(String, Bool)`:
```

```haskell
type Warrior = (String, Bool)

example = ("Warrior reading this kata", True)
```
```if:csharp
In C# the class `Person` is pre-loaded with the properties:
```

```csharp
public string Name { get; set; }
public bool WasNice { get; set; }
```

## Test Examples
```javascript
getNiceNames( [
    { name: 'Warrior reading this kata', wasNice: true },
    { name: 'xDranik', wasNice: false },
    { name: 'Santa', wasNice: true }
] )
// => returns [ 'Warrior reading this kata', 'Santa' ]

getNaughtyNames( [
    { name: 'Warrior reading this kata', wasNice: true },
    { name: 'xDranik', wasNice: false },
    { name: 'Santa', wasNice: true }
] )
// => returns [ 'xDranik' ]
```
```haskell
warriors = [
    ("xDranik",                   False),
    ("Santa",                     True), 
    ("Warrior reading this kata", True)
  ]
getNiceNames    warriors == ["Santa", "Warrior reading this kata"]
getNaughtyNames warriors == ["xDranik"]
```

```python
get_nice_names( [
    { 'name': 'Warrior reading this kata', 'was_nice': True },
    { 'name': 'xDranik', 'was_nice': False },
    { 'name': 'Santa', 'was_nice': True }
] )
# => returns [ 'Warrior reading this kata', 'Santa' ]
```

