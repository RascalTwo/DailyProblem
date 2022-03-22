[_metadata_:generated]: - "true"

# Classic Hello World

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57036f007fd72e3b77000023`](https://www.codewars.com/kata/57036f007fd72e3b77000023) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You are given a method called `main`, make it print the line `Hello World!`, (yes, that includes a new line character at the end) and don't return anything

Note that for some languages, the function `main` is the entry point of the program.

Here's how it will be tested:
```java
    java Solution.class parameter1 parameter2
```    

```javascript
    Solution.main("parameter1","parameter2");
```  

```coffeescript
    Solution.main "parameter1", "parameter2","parametern"
```

```ruby
    Solution.main("parameter1", "parameter2","parametern")
```

```python
    Solution.main("parameter1", "parameter2","parametern")
```

```csharp
   Solution.Main("parameter1", "parameter2","parametern")
```

```php
   Solution::main("parameter1", "parameter2", "parametern")
```
```sh
   no extra lines there
```

```prolog
   greet:greet
```

Hints:

 1. Check your references 
 2. Think about the scope of your method
 3. For prolog you can use write but there are [better ways](https://gist.github.com/dtonhofer/20bd01f68a924912771d8405fca66a09)
 4. If you still don't get it probably you can define main as an attribute of the Solution class that accepts a single argument, and that only prints "Hello World!" without any return.
