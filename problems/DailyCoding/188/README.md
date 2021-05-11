[_metadata_:number]:-      "188"
[_metadata_:difficulty]:-  "Medium"
[_metadata_:asker]:-       "Google"
[_metadata_:tags]:-        "function"

# 188

What will this code print out?

```
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
```

How can we make it print out what we apparently want?
