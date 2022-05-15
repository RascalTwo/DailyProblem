[_metadata_:generated]: - "true"

# Santa wish list form in ReactJS

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a9ecd89fd5777e0790001ea`](https://www.codewars.com/kata/5a9ecd89fd5777e0790001ea) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Santa wants to simplify his life and offer children the possiblity to enter their wishlist via an online form. 

The form should be a React component and should contain: 
 - an input field for the child's name (with id 'name')
 - a text area to describe the wish (id: 'wish')
 - a drop-down indicating the priority of the wish, from 1 to 5 - default is 1 (id: 'priority')
 - the keys in the state to store the corresponding values should be named the same as the element's id
 - an `onSubmit` action calling the function `handleSubmit`
 - a function called `handleSubmit`, which
   - calls `send` (a function that is already provided as part of the injected properties `props`)
   - passes the current state as a parameter to `send`
   - calls `event.preventDefault`
 - it should be a controlled component (i.e. using `onChange` to bind input to the component's state)
 
Further reading:
 - React Forms: https://reactjs.org/docs/forms.html
 - Learn about Controlled Components: https://www.codewars.com/kata/control-the-beast-controlled-components-in-reactjs
 
 

