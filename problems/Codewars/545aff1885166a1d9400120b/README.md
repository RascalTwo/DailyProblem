[_metadata_:generated]: - "true"

# Enumerable Magic #26 - Grab Elements While...

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                  |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`545aff1885166a1d9400120b`](https://www.codewars.com/kata/545aff1885166a1d9400120b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924090/ruby_v4klwh.svg" alt="Ruby" title="Ruby" width="50" />](solve.rb) |

<!-- INFO TABLE END -->

Create a method **take_while** that accepts a list and a block, and returns a array of the first several elements from the list, for as long as the block returns true.

Keep in mind, we don't want all the items for which the block returns true; once we get a false response, we want to stop looking. So this example:

    take_while([0,1,2,3,4,5,6]){|item| item.even?}
    
Will only return **[0]**, not **[0,2,4,6]**.

If you need help, here's a reference:

http://www.rubycuts.com/enum-take-while
