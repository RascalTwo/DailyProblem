[_metadata_:generated]: - "true"

# PC upgrade specs using HOC in ReactJS

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a9c0fa45084d79b1f000138`](https://www.codewars.com/kata/5a9c0fa45084d79b1f000138) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

First steps to learning the basics of higher order components (HOC) in ReactJS

A HOC is a _function_ that takes a _component_ as the first parameter and returns a _function_ wrapping the first parameter.

```javascript
function withExample(Component) {
  return function(props) {
    return <Component />
  }
}
```

More about HOC: [ReactJS docs](https://reactjs.org/docs/higher-order-components.html).

If you complete this kata try [Truncate paragraph using HOC in React JS](https://www.codewars.com/kata/truncate-paragraph-using-higher-order-component-in-react-js).

## Challenge

You're building a new feature on your e-commerce site which displays two computer specs - basic and pro.

The `PcDisplay` component is already built and expects 5 props. `{ title, price, cpu, ram, ssd }`

You will need to build a `withPriceModel` HOC and using that to manage the price of the `BasicModel` and `ProModel` components.

- Build a HOC called `withPriceModel` which takes the `PcDisplay` component for first param and price increase number for the second param.

- `withPriceModel` will manage the price and must set a default price of 50.

- `BasicModel` should use the default price set by `withPriceModel`

- `ProModel` should use `withPriceModel` to increase the price by 60. Total price should be 110.

- Since the `withPriceModel` is responsible for managing the price, ensure that it can't be overritten by passing in a price prop.

