[_metadata_:generated]: - "true"

# Simple Web Framework #1: Create a basic router

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`588a00ad70720f2cd9000005`](https://www.codewars.com/kata/588a00ad70720f2cd9000005) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this Kata, you have to design a simple routing class for a web framework.

The router should accept bindings for a given url, http method and an action. 

Then, when a request with a bound url and method comes in, it should return the result of the action.

Example usage:

```python
router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')

router.runRequest('/hello', 'GET') // returns 'hello world'
```
```javascript
var router = new Router;
router.bind('/hello', 'GET', function(){ return 'hello world'; });

router.runRequest('/hello', 'GET') // returns 'hello world';
```
```coffeescript
router = new Router
router.bind '/hello', 'GET', -> 'hello world'

router.runRequest '/hello', 'GET' # returns 'hello world'
```
```groovy
router = new Router()
router.bind("/hello", "GET", { -> "hello world" })
router.runRequest("/hello", "GET")  // returns "hello world"
```

```scala
router = new Router()
router.bind("/hello", "GET", () => "hello world")
router.runRequest("/hello", "GET")  // returns "hello world"
```

When asked for a route that doesn't exist, router should return:

```javascript
'Error 404: Not Found'
```
```python
'Error 404: Not Found'
```
```groovy
"Error 404: Not Found"
```
```scala
"Error 404: Not Found"
```

The router should also handle modifying existing routes. See the example tests for more details.

