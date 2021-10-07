# Generate Possible Playlists

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are going on a road trip, and would like to create a suitable music playlist.

The trip will require `N` songs, though you only have `M` songs downloaded, where `M` < `N`.

A valid playlist should select each song at least once, and guarantee a buffer of `B` songs between repeats.

Given `N`, `M`, and `B`, determine the number of valid playlists.

## Examples

| Input                                                                                                               | Output  |
| ------------------------------------------------------------------------------------------------------------------- | ------- |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`4`</td><td>`1`</td><td>`1`</td></tr></table> | `0`     |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`4`</td><td>`1`</td><td>`0`</td></tr></table> | `1`     |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`4`</td><td>`2`</td><td>`1`</td></tr></table> | `2`     |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`4`</td><td>`2`</td><td>`0`</td></tr></table> | `16`    |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`6`</td><td>`2`</td><td>`0`</td></tr></table> | `64`    |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`9`</td><td>`2`</td><td>`0`</td></tr></table> | `512`   |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`9`</td><td>`3`</td><td>`0`</td></tr></table> | `19683` |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`9`</td><td>`3`</td><td>`1`</td></tr></table> | `768`   |
| <table><tr><th>required</th><th>songs</th><th>buffer</th></tr><tr><td>`9`</td><td>`3`</td><td>`2`</td></tr></table> | `6`     |
