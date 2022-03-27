[_metadata_:generated]: - "true"

# Heads and Legs

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`574c5075d27783851800169e`](https://www.codewars.com/kata/574c5075d27783851800169e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

#Description

Everybody has probably heard of the animal heads and legs problem from the earlier years at school. It goes:

```“A farm contains chickens and cows. There are x heads and y legs. How many chickens and cows are there?” ```

Where x <= 1000 and y <=1000

#Task

Assuming there are no other types of animals, work out how many of each animal are there. 

```Return a tuple in Python - (chickens, cows) and an array list - [chickens, cows]/{chickens, cows} in all other languages```

If either the heads & legs is negative, the result of your calculation is negative or the calculation is a float return "No solutions" (no valid cases), or [-1, -1] in COBOL.


In the form:
```python
(Heads, Legs) = (72, 200)

VALID - (72, 200) =>             (44 , 28) 
                             (Chickens, Cows)

INVALID - (72, 201) => "No solutions"
```
```javascript
[Heads, Legs] = [72, 200]

VALID - [72, 200] =>             [44 , 28]   
                             [Chickens, Cows]

INVALID - [72, 201] => "No solutions"
```
```ruby
[Heads, Legs] = [72, 200]

VALID - [72, 200] =>             [44 , 28]   
                             [Chickens, Cows]

INVALID - [72, 201] => "No solutions"
```

```cobol
      Heads = 72
      Legs  = 200
      =>
      Chickens = 44
      Cows     = 28
      
      Heads = 72
      Legs  = 201
      =>
      Chickens = -1
      Cows     = -1
```

However, ```if 0 heads and 0 legs are given always return [0, 0]``` since zero heads must give zero animals.


There are many different ways to solve this, but they all give the same answer.

You will only be given integers types - however negative values (edge cases) will be given. 


Happy coding!
