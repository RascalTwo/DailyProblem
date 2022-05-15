[_metadata_:generated]: - "true"

# ES2015: Get the real length of string. 

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`599c4b69eb8e49effa000079`](https://www.codewars.com/kata/599c4b69eb8e49effa000079) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In es5, if the code point of a charactor is large than 0xFFFF will be treat as more than one charactor.

> Even codewars can't display emoji correctly.

For example:

The code point of an emoji  （big laugh: '\u{1f602}'）is 0x1f602.

So you will see:

```javascript
''.length
// 2
```

> Note: some emoji have more than one codepoint like  (China: '\u{1F1E8}\u{1F1F3}')，which is 0x1F1E8 0x1F1F3. This kata do not consider this situation for now.

And some chinese characters like Y which code point is 0x20059.

```
'Y'.length
// 2
```

We want get the real length of string.  

You need to write a function named `getRealLength` to get it.
