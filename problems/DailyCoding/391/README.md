# Common URL History

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

We have some historical clickstream data gathered from our site anonymously using cookies.

The histories contain URLs that users have visited in chronological order.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appear in both.

## Examples

| Input                                                                                                                | Output                        |
| -------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `[['/home', '/register', '/login', '/user', '/one', '/two'], ['/home', '/red', '/login', '/user', '/one', '/pink']]` | `['/login', '/user', '/one']` |
