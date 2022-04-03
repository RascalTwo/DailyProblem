[_metadata_:generated]: - "true"

# Person Class Bug

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                                                                                                                                                  |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`513f887e484edf3eb3000001`](https://www.codewars.com/kata/513f887e484edf3eb3000001) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924090/ruby_v4klwh.svg" alt="Ruby" title="Ruby" width="50" />](solve.rb) |

<!-- INFO TABLE END -->

The following code was thought to be working properly, however when the code tries to access the age of the person instance it fails. 

```ruby
person = Person.new('Yukihiro', 'Matsumoto', 47)
puts person.full_name
puts person.age
```
```python
person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)
```

For this exercise you need to fix the code so that it works correctly.
