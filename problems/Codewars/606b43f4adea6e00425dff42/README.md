[_metadata_:generated]: - "true"

# Map over a list of lists

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`606b43f4adea6e00425dff42`](https://www.codewars.com/kata/606b43f4adea6e00425dff42) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function which maps a function over the lists in a list:
```ruby
def grid_map inp,&block
  # applies the &block to all nested elements
```
```haskell
gridMap :: (a -> b) -> [[a]] -> [[b]]
```
```python
def grid_map(inp, op)
    # which performs op(element) for all elements of inp
```
```javascript
function gridMap(fn,xss) { return [[]]; }
```
```java
public static <T,R> R[][] gridMap(Function<T,R> fn, T[][] list)
```

Example 1:
```ruby
x = [[1,2,3],
     [4,5,6]]
     
grid_map(x) { |n| n + 1 }
#-- returns [[2,3,4],[5,6,7]]

grid_map(x) { |n| n ** 2 }
#-- returns [[1,4,9],[16,25,36]]
```
```haskell
x = [[1,2,3],
     [4,5,6]]
     
gridMap (+1) x
-- returns [[2,3,4],[5,6,7]]

gridMap (^2) x
-- returns [[1,4,9],[16,25,36]]
```
```python
x = [[1,2,3],
     [4,5,6]]
     
grid_map(x, lambda x: x + 1)
-- returns [[2,3,4],[5,6,7]]

grid_map(x, lambda x: x ** 2)
-- returns [[1,4,9],[16,25,36]]
```
```javascript
const xss = [ [1,2,3]
            , [4,5,6]
            ];

gridMap( x => x+1 , xss )  =>  [[2,3,4],[5,6,7]]
gridMap( x => x**2 , xss )  =>  [[1,4,9],[16,25,36]]
```
```java
int[][] x = {{1,2,3},
             {4,5,6}};

gridMap(e -> e + 1, x); // {{2,3,4},{5,6,7}}
gridMap(e -> e * e, x); // {{1,4,9},{16,25,36}}
```

Example 2
```ruby
x = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
     
grid_map(x) { |c| c.upcase }
#-- returns [["H", "E", "L", "L", "O"], ["W", "O", "R", "L", "D"]]

```
```haskell
import Data.Char
x = ["hEllO", "wOrLd"]

gridMap toUpper x
-- returns ["HELLO, WORLD"]
```
```python
x = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
grid_map(x, lambda x: x.upper())
-- returns [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']]
```
```javascript
const xss = [['h','E','l','l','O'],['w','O','r','L','d']];

gridMap( x => x.toUpperCase() , xss )  =>  [['H','E','L','L','O'],['W','O','R','L','D']]
```
```java
char[][] x = {{'h','E','l','l','O'},{'w','O','r','L','d'}};

gridMap(e -> Character.toUpperCase(e), x); // {{'H','E','L','L','O'},{'W','O','R','L','D'}}
```
