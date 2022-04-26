[_metadata_:generated]: - "true"

# Make them bark!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5535572c1de94ba2db0000f6`](https://www.codewars.com/kata/5535572c1de94ba2db0000f6) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

#Make them bark

You have been hired by a dogbreeder to write a program to keep record of his dogs.

You've already made a constructor `Dog`, so no one has to hardcode every puppy.

The work seems to be done. It's high time to collect the payment.

..hold on! The dogbreeder says he wont pay you, until he can make every dog object `.bark()`. Even the ones already done with your constructor.
"Every dog barks" he says. He also refuses to rewrite them, lazy as he is.

You can't even count how much objects that bastard client of yours already made. He has a lot of dogs, and none of them can `.bark()`. 

Can you solve this problem, or will you let this client outsmart you for good?

### Practical info:

 - The `.bark()` method of a dog should return the string `'Woof!'`.

 - The contructor you made (it is preloaded) looks like this:

```javascript
function Dog(name, breed, sex, age){
    this.name  = name;
    this.breed = breed;
    this.sex   = sex;
    this.age   = age;
}
```
```coffeescript
class Dog
    constructor: (@name, @breed, @sex, @age) ->
```
```python
class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age
```
```ruby
class Dog
  def initialize(name, breed, sex, age)
     @name = name
     @breed = breed
     @sex = sex
     @age = age
  end
end
```

>**Hint:** A friend of yours just told you about how javascript handles classes diferently from other programming languages. He couldn't stop ranting about *"prototypes"*, or something like that. Maybe that could help you...
