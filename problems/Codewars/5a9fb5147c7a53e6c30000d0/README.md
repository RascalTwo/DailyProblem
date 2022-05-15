[_metadata_:generated]: - "true"

# Unshackle the Beast (uncontrolled components in ReactJS)

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a9fb5147c7a53e6c30000d0`](https://www.codewars.com/kata/5a9fb5147c7a53e6c30000d0) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this kata you'll learn how to use uncontrolled components in ReactJS with different kinds of chained beasts.
Your goal is to release a beast by building an uncontrolled React component with the following criteria:
- Create a component called `BeastForm`.
- This component should have a `beastToRelease` property which is an object.
- The initial beast will be assigned by setting the `value` property of the `beastToRelease` object.
- The beast can be passed into the input element with the id `beastToRelease` living in a form element with the id `beastForm`.
- The form needs to be submitted with a submit button with the id `submit` and call a function to handle the form submission.
- This function needs to call an already existing function `unshackle` with the beast to release. 
- This function also needs to call `preventDefault` on the passed parameter. 

Read about uncontrolled components here: https://reactjs.org/docs/uncontrolled-components.html

