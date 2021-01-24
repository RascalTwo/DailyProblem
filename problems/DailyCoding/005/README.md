[_metadata_:number]:-      "5"
[_metadata_:difficulty]:-  "Medium"
[_metadata_:asker]:-       "Jane"
[_metadata_:tags]:-        "function"

# 005

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement car and cdr.
