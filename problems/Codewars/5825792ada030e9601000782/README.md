[_metadata_:generated]: - "true"

# zipWith

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5825792ada030e9601000782`](https://www.codewars.com/kata/5825792ada030e9601000782) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Task

`zipWith` ( or `zip_with` ) takes a function and two arrays and zips the arrays together, applying the function to every pair of values.  
The function value is one new array.

If the arrays are of unequal length, the output will only be as long as the shorter one.  
(Values of the longer array are simply not used.)

Inputs should not be modified.

## Examples

```c
zip_with(pow,4,{10,10,10,10},4,{0,1,2,3},*z,*a) =>
a = {1,10,100,1000}
z = 4
zip_with(max,3,{2,7,5},5,{8,7,4,1,3},*z,*a)     =>
a = {8,7,5}
z = 3
```
```javascript
zipWith( Math.pow, [10,10,10,10], [0,1,2,3] )      =>  [1,10,100,1000]
zipWith( Math.max, [1,4,7,1,4,7], [4,7,1,4,7,1] )  =>  [4,7,7,4,7,7]

zipWith( function(a,b) { return a+b; }, [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  // Both forms are valid
zipWith( (a,b) => a+b,                  [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  // Both are functions
```
```python
zip_with( pow, [10,10,10,10], [0,1,2,3] )     =>  [1,10,100,1000]
zip_with( max, [1,4,7,1,4,7], [4,7,1,4,7,1])  =>  [4,7,7,4,7,7]

def add(a,b): return a+b; # or from operator import add
zip_with( add,             [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  # Both forms are valid
zip_with( lambda a,b: a+b, [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  # Both are functions
```
```rust
zip_with(i32::pow, &[10,10,10,10], [0,1,2,3])     => [1,10,100,1000]
zip_with(i32::max, &[1,4,7,1,4,7], [4,7,1,4,7,1]) => [4,7,7,4,7,7]

fn add(a: i32, b: i32) -> i32 { a + b }  // or i32::add
zip_with(add, &[0,1,2,3], &[0,1,2,3])         => [0,2,4,6]  // Both forms are valid
zip_with(|a,b| a + b, &[0,1,2,3], &[0,1,2,3]) => [0,2,4,6]  // Both are functions
```
```ocaml
zip_with ( * ) [10; 10; 10; 10] [0; 1; 2; 3] (* = [0; 10; 20; 30] *)
zip_with max [1; 4; 7; 1; 4; 7] [4; 7; 1; 4; 7; 1] (* = [4; 7; 7; 4; 7; 7] *)

zip_with        (+)         [0; 1; 2; 3] [0; 1; 2; 3] (* = [0; 2; 4; 6] *)
zip_with (fun a b -> a + b) [0; 1; 2; 3] [0; 1; 2; 3] (* = [0; 2; 4; 6] *)
```

## Input validation

Assume all input is valid.

