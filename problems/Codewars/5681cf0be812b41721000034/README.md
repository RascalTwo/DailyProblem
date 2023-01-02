[_metadata_:generated]: - "true"

# Remove the noise from the string

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5681cf0be812b41721000034`](https://www.codewars.com/kata/5681cf0be812b41721000034) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

We have a broken message machine that introduces noise to our incoming messages. We know that our messages can't be written using `%$&/#·@|º\ª` and white characters (like spaces or tabs). Unfortunately our machine introduces noise, which means that our message arrives with characters like: `%$&/#·@|º\ª` within our original message.

Your mission is to write a function which removes this noise from the message.

> Notice that noise can only be **`%$&/#·@|º\ª`** characters, other characters are not as considered noise

For example:

```ruby
remove_noise("H%e&%$llo w&%or&$l$%d!")
# returns 'Hello world!'

# In order to keep the level of this Kata, in ruby version noise can have only `%$&/#@|\` chars.
````

```javascript
removeNoise("h%e&·%$·llo w&%or&$l·$%d")
// returns hello world
```

```coffeescript
removeNoise "h%e&·%$·llo w&%or&$l·$%d"
// returns hello world
```

```csharp
Kata.removeNoise("h%e&·%$·llo w&%or&$l·$%d")
// returns hello world
```

```csharp
removeNoise "h%e&·%$·llo w&%or&$l·$%d"
// returns hello world
```
