[_metadata_:number]:-      "139"
[_metadata_:difficulty]:-  "Medium"
[_metadata_:asker]:-       "Google"
[_metadata_:tags]:-        "data-structure"

# 139

Given an iterator with methods `next()` and `hasNext()`, create a wrapper iterator, `PeekableInterface`, which also implements `peek()`. peek shows the next element that would be returned on `next()`.

Here is the interface:

```python
class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
```