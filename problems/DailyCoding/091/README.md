[_metadata_:difficulty]:-  "Easy"
[_metadata_:asker]:-       "Dropbox"
[_metadata_:tags]:-        "function"

# 091

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

```python
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
```
