[_metadata_:generated]: - "true"

# Can you keep a secret?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5351b35ebaeb67f9110012d2`](https://www.codewars.com/kata/5351b35ebaeb67f9110012d2) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

There's no such thing as private properties on a coffeescript object!
But, maybe there are?

Implement a function `createSecretHolder(secret)` which accepts any value as secret and returns an object with __ONLY__ two methods

* `getSecret()` which returns the secret 
* `setSecret()` which sets the secret

```coffeescript
obj = createSecretHolder(5)
obj.getSecret() # returns 5
obj.setSecret(2)
obj.getSecret() # returns 2
```

  

