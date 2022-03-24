[_metadata_:generated]: - "true"

# Enumerable Magic #30 - Split that Array!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                        |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`545b342082e55dc9da000051`](https://www.codewars.com/kata/545b342082e55dc9da000051) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Create a method **partition** that accepts a list and a method/block. It should return two arrays: the first, with all the elements for which the given block returned true, and the second for the remaining elements.

Here's a simple Ruby example:

    animals = ["cat", "dog", "duck", "cow", "donkey"]
    partition(animals){|animal| animal.size == 3}
        #=> [["cat", "dog", "cow"], ["duck", "donkey"]]

The equivalent in Python would be:

    animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
    partition(animals, lambda x: len(x) == 3)
        # (['cat', 'dog', 'cow'], ['duck', 'donkey'])

If you need help, here's a reference:

http://www.rubycuts.com/enum-partition
