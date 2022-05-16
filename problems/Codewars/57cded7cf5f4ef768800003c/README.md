[_metadata_:generated]: - "true"

# Fix the base conversion function!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                        |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57cded7cf5f4ef768800003c`](https://www.codewars.com/kata/57cded7cf5f4ef768800003c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Poor Cade has got his number conversions mixed up again!

Fix his ```convert_num()``` function so it correctly converts a base-10 ```int```eger, 
to the selected of ```bin```ary or ```hex```adecimal.

```#The output should be a string at all times```

```python
convert_num(number, base):
    if 'base' = hex:
        return int(number, 16)
    if 'base' = bin:
        return int(number, 2)
    return (Incorrect base input)
```
Please note, invalid ```number``` or ```base``` inputs will be tested.
In the event of an invalid ```number/base``` you should return:
```python
"Invalid number input"
or
"Invalid base input"
```
For each respectively.

Good luck coding! :D
