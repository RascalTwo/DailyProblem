[_metadata_:generated]: - "true"

# Batman Quotes

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`551614eb77dd9ee37100003e`](https://www.codewars.com/kata/551614eb77dd9ee37100003e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Batman & Robin have gotten into quite a pickle this time. The Joker has mixed up their iconic quotes and also replaced one of the characters in their names, with a number. They need help getting things back in order.

Implement the getQuote method which takes in an array of quotes, and a string comprised of letters and a single number (e.g. "Rob1n") where the number corresponds to their quote indexed in the passed in array.

Return the quote along with the character who said it:

```java
BatmanQuotes.getQuote(["I am vengeance. I am the night. I am Batman!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"], "Rob1n") should output =>  "Robin: Holy haberdashery, Batman!
```

```javascript
getQuote(["I am vengeance. I am the night. I am Batman!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"], "Rob1n") 
  // =>  "Robin: Holy haberdashery, Batman!
```


```clojure
(getQuote ["I am vengeance. I am the night. I am Batman!" "Holy haberdashery, Batman!" "Let's put a smile on that faaaceee!"] "Rob1n") 
  // =>  "Robin: Holy haberdashery, Batman!"
```

Hint: You are guaranteed that the number in the passed in string is placed somewhere after the first character of the string. The quotes either belong to "Batman", "Robin", or "Joker".
