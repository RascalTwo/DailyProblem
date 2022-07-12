[_metadata_:generated]: - "true"

# First-Class Function Factory

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`563f879ecbb8fcab31000041`](https://www.codewars.com/kata/563f879ecbb8fcab31000041) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function, `factory`, that takes a number as its parameter and returns another function.

The returned function should take an array of numbers as its parameter, and return an array of those numbers *multiplied by the number that was passed into the first function*.

In the example below, 5 is the number passed into the first function. So it returns a function that takes an array and multiplies all elements in it by five.

Translations and comments (and upvotes) welcome!

## Example
```javascript
var fives = factory(5);       // returns a function - fives
var myArray = [1, 2, 3];
fives(myArray);               //returns [5, 10, 15];
```
```python
fives = factory(5)          # returns a function - fives
my_array = [1, 2, 3]
fives(my_array)             # returns [5, 10, 15]
```
```coffeescript
fives = factory(5)          # returns a function - fives
myArray = [1, 2, 3]
fives(myArray)             # returns [5, 10, 15]
```
```haskell
let fives = factory 5      -- returns a function - fives
fives [1, 2, 3]            -- returns [5, 10, 15]
```
```csharp
Func<int[],int[]> fives = FunctionFactory.factory(5);    // returns a function - fives
int[] myArray = new int[]{1, 2, 3};
fives(myArray);                  //returns [5, 10, 15];
```
```clojure
(let [fives (factory 5)]      ; returns a function - fives
  (fives [1 2 3]))            ; returns [5 10 15]
```
```factor
{ 1 2 3 }
5 factory              ! returns a quotation
call( seq -- newseq )  ! returns { 5 10 15 }
```
