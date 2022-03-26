[_metadata_:generated]: - "true"

# Unexpected parsing

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                        |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54fdaa4a50f167b5c000005f`](https://www.codewars.com/kata/54fdaa4a50f167b5c000005f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Here is a piece of code:
```javascript
function getStatus(isBusy) {
  var msg = (isBusy ? "busy" : "available");
  return 
  {
    status: msg
  }
}
```

```python
def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return status
```

```ruby
def get_status(is_busy)
    status = is_busy ? "busy" : "available"
    return status
end
```

## Expected Behaviour
Function should return a dictionary/Object/Hash with `"status"` as a key, whose value can : `"busy"` or `"available"` depending on the truth value of the argument `is_busy`.

But as you will see after clicking `RUN` or `ATTEMPT` this code has several bugs, please fix them.


