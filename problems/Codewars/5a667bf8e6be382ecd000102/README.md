[_metadata_:generated]: - "true"

# Truncate paragraph using higher-order component in React JS

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a667bf8e6be382ecd000102`](https://www.codewars.com/kata/5a667bf8e6be382ecd000102) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Learn how to make a React JS higher-order component (HOC) and follow good practice.

A HOC is a _function_ that takes a _component_ as the first parameter and returns a _function_ wrapping the first parameter.

```javascript
function withExample(Component) {
  return function(props) {
    return <Component />
  }
}
```

Just getting started on HOC? **Try [PC upgrade specs using HOC in ReactJS](https://www.codewars.com/kata/pc-upgrade-specs-using-hoc-in-reactjs) kata**

Not sure what it's all about see my post about it: [Understanding higher-order component](http://www.richardkotze.com/coding/understanding-higher-order-components) and [ReactJS docs](https://reactjs.org/docs/higher-order-components.html).

## Your challenge:

Truncate a paragraph of text for elements that contain `props.children` of type `String`

- Create a HOC
- Should read `props.children` and truncate to the specified length
- A `textLength` prop will be passed in to specify where to cut the text to
- Default `textLength` is 10
- If `textLength` is -1 then render `props.children` as is without truncating.
- Should be able to pass additional props through
- HOC should have correctly formatted displayName `WithTruncateParagraph(ComponentName)` _as shown in React docs_

Enjoy :)


