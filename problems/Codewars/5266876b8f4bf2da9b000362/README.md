[_metadata_:generated]: - "true"

# Who likes it?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                                                                                                                                                            |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5266876b8f4bf2da9b000362`](https://www.codewars.com/kata/5266876b8f4bf2da9b000362) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924086/php_wxp0v1.svg" alt="PHP" title="PHP" width="50" />](solve.php) |

<!-- INFO TABLE END -->

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

```
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```


```if:c
* return must be an allocated string
* do not mutate input
```

Note: For 4 or more names, the number in `"and 2 others"` simply increases.

