[_metadata_:generated]: - "true"

# isReallyNaN

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56c24c58e0c0f741d4001aef`](https://www.codewars.com/kata/56c24c58e0c0f741d4001aef) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

I've hit a few bugs in my Java/Type/Coffee-script  code recently, and I've traced the problem back to the global `isNaN` function I was using. I had expected it to be more discerning, but it's returning true for `undefined` right now.

Write a function `isReallyNaN` that returns `true` only if passed in an argument that evalutes to `NaN`, and returns `false` otherwise.

Any solution is acceptable!
