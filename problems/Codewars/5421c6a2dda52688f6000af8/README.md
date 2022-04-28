[_metadata_:generated]: - "true"

# Function Composition

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5421c6a2dda52688f6000af8`](https://www.codewars.com/kata/5421c6a2dda52688f6000af8) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

__Function composition__ is a mathematical operation that mainly presents itself in lambda calculus and computability. It is explained well [here](http://www.mathsisfun.com/sets/functions-composition.html), but this is my explanation, in simple mathematical notation:

```
f3 = compose( f1 f2 )
   Is equivalent to...
f3(a) = f1( f2( a ) )
```
~~~if-not:lambdacalc,ruby
Your task is to create a `compose` function to carry out this task, which will be passed two functions or lambdas. Ruby functions will be passed, and should return, either a proc or a lambda. Remember that the resulting composed function may be passed multiple arguments!
~~~
~~~if:ruby
Your task is to create a `compose` function to carry out this task, which will be passed two functions, and should return either a proc or a lambda. Remember that the resulting composed function may be passed multiple arguments!
~~~
~~~if:lambdacalc
Your task is to create a `compose` function to carry out this task.
~~~
```javascript
compose(f , g)(x)
=> f( g( x ) )
```
```ruby
compose(f , g).(x)
=> f.( g.( x ) )
```
```coffeescript
compose(f , g)(x)
=> f( g( x ) )
```
```clojure
((compose f  g) x)
=> (f (g x) )
```
```python
compose(f , g)(x)
=> f( g( x ) )
```
```lambdacalc
h = compose f g
h x # f (g x)
```


This kata is not available in haskell; that would be too easy!
