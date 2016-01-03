[_metadata_:generated]: - "true"

# Building blocks

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55b75fcf67e558d3750000a3`](https://www.codewars.com/kata/55b75fcf67e558d3750000a3) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/java_un8ru7.svg" alt="Java" title="Java" width="50" />](class.java) |

<!-- INFO TABLE END -->

Write a class `Block` that creates a block (Duh..)

##Requirements

The constructor should take an array as an argument,
this will contain 3 integers of the form `[width, length, height]` from which the `Block` should be created.

Define these methods:

```python
`get_width()` return the width of the `Block`

`get_length()` return the length of the `Block`

`get_height()` return the height of the `Block`

`get_volume()` return the volume of the `Block`

`get_surface_area()` return the surface area of the `Block`
```

```ruby
`get_width()` return the width of the `Block`

`get_length()` return the length of the `Block`

`get_height()` return the height of the `Block`

`get_volume()` return the volume of the `Block`

`get_surface_area()` return the surface area of the `Block`
```
```java
`getWidth()` return the width of the `Block`

`getLength()` return the length of the `Block`

`getHeight()` return the height of the `Block`

`getVolume()` return the volume of the `Block`

`getSurfaceArea()` return the surface area of the `Block`
```
```javascript
`getWidth()` return the width of the `Block`

`getLength()` return the length of the `Block`

`getHeight()` return the height of the `Block`

`getVolume()` return the volume of the `Block`

`getSurfaceArea()` return the surface area of the `Block`
```
```coffeescript
`getWidth()` return the width of the `Block`

`getLength()` return the length of the `Block`

`getHeight()` return the height of the `Block`

`getVolume()` return the volume of the `Block`

`getSurfaceArea()` return the surface area of the `Block`
```
```haskell
`getWidth()` return the width of the `Block`

`getLength()` return the length of the `Block`

`getHeight()` return the height of the `Block`

`getVolume()` return the volume of the `Block`

`getSurfaceArea()` return the surface area of the `Block`
```
```csharp
`GetWidth()` return the width of the `Block`

`GetLength()` return the length of the `Block`

`GetHeight()` return the height of the `Block`

`GetVolume()` return the volume of the `Block`

`GetSurfaceArea()` return the surface area of the `Block`
```

##Examples

```python
    b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a height of `6`
    
    b.get_width() -> return 2
    
    b.get_length() -> return 4
    
    b.get_height() -> return 6
    
    b.get_volume() -> return 48
    
    b.get_surface_area() -> return 88
```
```javascript
    let b = new Block([2,4,6]) -> creates a `Block` object with a width of `2` a length of `4` and a height of `6`
    b.getWidth() // -> 2
    
    b.getLength() // -> 4
    
    b.getHeight() // -> 6
    
    b.getVolume() // -> 48
    
    b.getSurfaceArea() // -> 88
```
```coffeescript
    b = new Block [2,4,6] #  creates a `Block` object with width of `2`,
                          #  length of `4`, and height of `6`
    b.getWidth()          # 2
    b.getLength()         # 4
    b.getHeight()         # 6
    b.getVolume()         # 48
    b.getSurfaceArea()    # 88
```
```ruby
    b = Block.new([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a height of `6`
    
    b.get_width() -> return 2
    
    b.get_length() -> return 4
    
    b.get_height() -> return 6
    
    b.get_volume() -> return 48
    
    b.get_surface_area() -> return 88
```
```haskell
  b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a height of `6`
```
```csharp
    Block b = new Block(new int[]{2,4,6}) -> creates a `Block` object with a width of `2` a length of `4` and a height of `6`
    b.GetWidth() // -> 2
    
    b.GetLength() // -> 4
    
    b.GetHeight() // -> 6
    
    b.GetVolume() // -> 48
    
    b.GetSurfaceArea() // -> 88
```
```java
    Block b = new Block(new int[]{2,4,6}) -> creates a `Block` object with a width of `2` a length of `4` and a height of `6`
    b.getWidth() // -> 2
    
    b.getLength() // -> 4
    
    b.getHeight() // -> 6
    
    b.getVolume() // -> 48
    
    b.getSurfaceArea() // -> 88
```

Note: no error checking is needed

Any feedback would be much appreciated

