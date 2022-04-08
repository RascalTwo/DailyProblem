[_metadata_:generated]: - "true"

# Ruby Metaprogramming 101 - Dynamic Method Calls

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                  |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5ce55047cb83dc0024cfadc6`](https://www.codewars.com/kata/5ce55047cb83dc0024cfadc6) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924090/ruby_v4klwh.svg" alt="Ruby" title="Ruby" width="50" />](solve.rb) |

<!-- INFO TABLE END -->

In metaprogramming we'll sometimes define a method at runtime, and therefore won't know its name beforehand. Your task is to write a method that takes two arguments: an object, and a method name. 

The given method name will always be a symbol, and the receiving object will always know how to respond to the given method. The given method will never require any arguments.

Your method should return the result of calling `method` on `obj`.

For example, the following method call...

`dynamic_caller('zaphod!', :upcase)`

... should return `ZAPHOD!`
