[_metadata_:generated]: - "true"

# Find an employees role in the company

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55c9fb1b407024afe6000055`](https://www.codewars.com/kata/55c9fb1b407024afe6000055) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You get a new job working for Eggman Movers.  Your first task is to write a method that will allow the admin staff to enter a person’s name and return what that person's role is in the company.

You will be given an array of object literals holding the current employees of the company.  You code must find the employee with the matching firstName and lastName and then return the role for that employee or if no employee is not found it should return "Does not work here!"

The array is preloaded and can be referenced using the variable `employees` (`$employees` in Ruby). It uses the following structure.

```javascript
let employees = [ {firstName: "Dipper", lastName: "Pines", role: "Boss"}, ...... ]
```
```python
employees = [ {'first_name': "Dipper", 'last_name': "Pines", 'role': "Boss"}, ...... ]
```
```ruby
employees = [ {'first_name'=> "Dipper", 'last_name'=> "Pines", 'role'=> "Boss"}, ...... ]
```

There are no duplicate names in the array and the name passed in will be a single string with a space between the first and last name i.e. Jane Doe or just a name.
