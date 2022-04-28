[_metadata_:generated]: - "true"

# Password Hashes

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54207f9677730acd490000d1`](https://www.codewars.com/kata/54207f9677730acd490000d1) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

When you sign up for an account somewhere, some websites do not actually store your password in their databases.  Instead, they will transform your password into something else using a cryptographic hashing algorithm.

After the password is transformed, it is then called a *password hash*.  Whenever you try to login, the website will transform the password you tried using the same hashing algorithm and simply see if the password hashes are the same.

-----

Create the function that converts a given string into an `md5` hash.  The return value should be encoded in `hexadecimal`.

```if:javascript
Remember that you can include the builtin `require()` function to include external modules (you're not expected to implement MD5 hash algorithm yourself, there are many modules that can do that for you).

If you're not familiar with modules, see [this kata](https://www.codewars.com/kata/541db50c259d9c55c00007b9).

NodeJS documentation [here](https://nodejs.org/api/).
```

## Code Examples
```
passHash("password") // --> "5f4dcc3b5aa765d61d8327deb882cf99"
passHash("abc123") // --> "e99a18c428cb38d5f260853678922e03"
```
If you want to externally test a string, [look at this website](http://www.md5hasher.net/).


-----
As a side note, `md5` can be exploited, so never use it for anything secure.  The reason I used it in this kata is simply because it is a very common hashing algorithm and many people will recognize the name.
