[_metadata_:generated]: - "true"

# Born to be chained

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54c27ef1fb7da0118600046a`](https://www.codewars.com/kata/54c27ef1fb7da0118600046a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Function composition is a powerful technique. For example:

```javascript
function sum(x, y) {
  return x + y;
}

function double(x) {
  return sum(x, x);
}

function minus (x, y) {
  return x - y;
}

function addOne(x) {
  return sum(x, 1);
}

double(sum(2, 3)); // 10
```

But in complex expressions, composition may be difficult to understand. For example:

```javascript
double(double(addOne(sum(7, minus(sum(5, sum(4, 5)), 4))))); // 72
```

In this kata, we will implement a function that allows us to perform this by applying a fluid style:

```javascript
c.sum(4, 5).sum(5).minus(4).sum(7).addOne().double().double().execute(); // 72
```
Your job is implement the `chain` function:

```javascript
function chain(fns) {
}

var c = chain({sum: sum, minus: minus, double: double, addOne: addOne});
```
As you can see, this function receives the methods to be chained and returns an object that allows you to call the chained methods. The result is obtained by calling the `execute` method.

Chained functions receive an arbitrary number of arguments. The first function in the chain receives all its arguments. In the other functions, the first argument is the result of the previous function and then it only receives the remainder arguments (second, third, etc.). The tests always pass the appropriate arguments and you do not have to worry about checking this.


Note that the chain can be reused (the internal state is not stored):

```javascript
c.sum(3, 4).execute(); //7
c.sum(1, 2).execute(); //3
```

Other examples:

```javascript
var c1 = c.sum(1, 2);
c1.execute(); // == fns.sum(1, 2) == 3
c1.double().execute(); // == fns.double(fns.sum(1, 2)) == 6
c1.addOne().execute(); // == fns.addOne(fns.sum(1, 2)) == 4
c1.execute(); // == fns.sum(1, 2) == 3

var c2 = c1.sum(5);
c2.addOne().execute(); // == fns.addOne(fns.sum(fns.sum(1, 2) 5)) == 9
c2.sum(3).execute(); // == fns.sum(c1.sum(fns.sum(1, 2), 5), 3) == 11
c2.execute(); // == fns.sum(fns.sum(1, 2), 5) == 8

c1.execute(); // == fns.sum(1, 2) == 3
```


