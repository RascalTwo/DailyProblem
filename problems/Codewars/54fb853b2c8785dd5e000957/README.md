[_metadata_:generated]: - "true"

# Chain me

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54fb853b2c8785dd5e000957`](https://www.codewars.com/kata/54fb853b2c8785dd5e000957) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Write a generic function chainer

Write a generic function chainer that takes a starting value, and an array of functions to execute on it (array of symbols for Ruby).

The input for each function is the output of the previous function (except the first function, which takes the starting value as its input). Return the final value after execution is complete.

```javascript
function add(num) {
  return num + 1;
}

function mult(num) {
  return num * 30;
}

chain(2, [add, mult]);
// returns 90;
```
```haskell
add = (+ 1)
mul = (* 30)

chain 2 [add, mult] -> 90
```
```ruby
def add num
  num + 1
end

def mult num
  num * 30 
end

chain(2, [:add, :mult])
#=> returns 90
```
```csharp
double input = 2;

public static double add(double x) {
  return x + 1;
}

public static double mul(double x) {
   return x * 30;
}
Kata.Chain( input , new[] { (Func<double, double>)add, mul });
//=> returns 90
```

```c
int add10 (int x) { return x + 10; }
int mul30 (int x) { return x * 30; }

typedef int (*funcptr) (int);

chain(50, 2, (funcptr[2]) {add10, mul30});
// returns 1800
```
