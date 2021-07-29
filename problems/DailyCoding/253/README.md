# Zig-Zag string

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a string and a number of lines `height`, print the string in zigzag form.

In zigzag, characters are printed out diagonally from top left to bottom right until reaching the `height`th line, then back up to top right, and so on.

## Examples

Given the sentence `"thisisazigzag"` and `height = 4`, you should print:

    t     a     g
     h   s z   a
      i i   i z
       s     g

| Input                                                                                                 | Output                                                                             |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| <table><tr><th>string</th><th>height</th></tr><tr><td>`'thisisazigzag'`</td><td>`4`</td></tr></table> | `'t     a     g\n h   s z   a \n  i i   i z  \n   s     g   '`                     |
| <table><tr><th>string</th><th>height</th></tr><tr><td>`'thisisazigzag'`</td><td>`3`</td></tr></table> | `'t   i   i   g\n h s s z g a \n  i   a   z  '`                                    |
| <table><tr><th>string</th><th>height</th></tr><tr><td>`'thisisazigzag'`</td><td>`5`</td></tr></table> | `'t       i     \n h     z g    \n  i   a   z   \n   s s     a y\n    i       g '` |
