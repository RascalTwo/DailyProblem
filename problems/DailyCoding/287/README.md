# Calculate Website Similarity

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a list of `(website, user)` pairs that represent users visiting websites.

Come up with a program that identifies the top `k` pairs of websites with the greatest similarity.

For example, suppose `k = 1`, and the list of tuples is:

    [
      ('facebok', 1), ('facebok', 3), ('facebok', 5),
      ('rreddit', 2), ('rreddit', 6),
      ('twitter', 1), ('twitter', 2), ('twitter', 3), ('twitter', 4), ('twitter', 5),
      ('example', 4), ('example', 5), ('example', 6), ('example', 7),
      ('myspace', 1), ('myspace', 3), ('myspace', 5), ('myspace', 6)
    ]

Then a reasonable similarity metric would most likely conclude that `facebok` and `myspace` are the most similar, so your program should return `[('facebok', 'myspace')]`.

## Examples

| Input                                                                                                                                                                                                                                                                                                                                                                            | Output                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| <table><tr><th>sites</th><th>k</th></tr><tr><td>`[('facebok', 1), ('facebok', 3), ('facebok', 5), ('rreddit', 2), ('rreddit', 6), ('twitter', 1), ('twitter', 2), ('twitter', 3), ('twitter', 4), ('twitter', 5), ('example', 4), ('example', 5), ('example', 6), ('example', 7), ('myspace', 1), ('myspace', 3), ('myspace', 5), ('myspace', 6)]`</td><td>`1`</td></tr></table> | `[('facebok', 'myspace')]`                         |
| <table><tr><th>sites</th><th>k</th></tr><tr><td>`[('facebok', 1), ('facebok', 3), ('facebok', 5), ('rreddit', 2), ('rreddit', 6), ('twitter', 1), ('twitter', 2), ('twitter', 3), ('twitter', 4), ('twitter', 5), ('example', 4), ('example', 5), ('example', 6), ('example', 7), ('myspace', 1), ('myspace', 3), ('myspace', 5), ('myspace', 6)]`</td><td>`2`</td></tr></table> | `[('facebok', 'myspace'), ('facebok', 'twitter')]` |
