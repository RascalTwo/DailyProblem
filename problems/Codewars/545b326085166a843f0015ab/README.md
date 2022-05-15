[_metadata_:generated]: - "true"

# Enumerable Magic #29 - Grouping Elements Together

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                  |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`545b326085166a843f0015ab`](https://www.codewars.com/kata/545b326085166a843f0015ab) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924090/ruby_v4klwh.svg" alt="Ruby" title="Ruby" width="50" />](solve.rb) |

<!-- INFO TABLE END -->

Create a method **group_by** that accepts a list and a block. It should return a hash where the keys are the block return values, and the hash values are arrays of the corresponding items grouped together.

Here's a simple example:

    animals = ["cat", "dog", "duck", "cow", "donkey"]
    group_by(animals){|animal| animal[0]}
        #=> {"c" => ["cat", "cow"], "d" => ["dog", "duck", "donkey"]}

If you need help, here's a reference:

http://www.rubycuts.com/enum-group-by
