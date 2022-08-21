[_metadata_:generated]: - "true"

# Who has the most money?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`528d36d7cc451cd7e4000339`](https://www.codewars.com/kata/528d36d7cc451cd7e4000339) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

```ruby
class Student
  attr_reader :name
  attr_reader :fives
  attr_reader :tens
  attr_reader :twenties
  
  def initialize(name, fives, tens, twenties)
    @name = name
    @fives = fives
    @tens = tens
    @twenties = twenties
  end
end
```
```python
class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
```
```c
#define NAMELIM     0x8

struct student {
    char name[NAMELIM + 1];
    unsigned fives;
    unsigned tens;
    unsigned twenties;
};
```
```nasm
struc student
    .name:      resb 9
                alignb 4
    .fives:     resd 1
    .tens:      resd 1
    .twenties:  resd 1
endstruc

student_sz      equ 0h18
```
```javascript
class Student {
  constructor(name, fives, tens, twenties) {
    this.name = name;
    this.fives = fives;
    this.tens = tens;
    this.twenties = twenties;
  }
}
```
```scala
case class Student(name: String, fives: Int, tens: Int, twenties: Int)
```

As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return `"all"`.

Notes:
* Each student will have a unique name
* There will always be a clear winner: either one person has the most, or everyone has the same amount
* If there is only one student, then that student has the most money
