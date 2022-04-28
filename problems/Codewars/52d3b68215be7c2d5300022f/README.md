[_metadata_:generated]: - "true"

# Simple Events

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52d3b68215be7c2d5300022f`](https://www.codewars.com/kata/52d3b68215be7c2d5300022f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Your goal is to write an __Event__ constructor function, which can be used to make __event__ objects.

An __event__ object should work like this:

  - it has a    __.subscribe()__ method, which takes a function and stores it as its handler
  - it has an __.unsubscribe()__ method, which takes a function and removes it from its handlers
  - it has an __.emit()__ method, which takes an arbitrary number of arguments and calls all the stored functions  with these arguments

As this is an elementary example of events, there are some simplifications:
   
  - all functions are called with correct arguments (_e.g._ only  functions will be passed to unsubscribe)
  - you should not worry about the order of handlers' execution
  - the handlers will not attempt to modify an event object (_e.g._ add or remove handlers)
  - the context of handlers'  execution is not important
  - each handler will be subscribed at most once at any given moment of time. It can still be unsubscribed and then subscribed again

Also see an example test fixture for suggested usage
