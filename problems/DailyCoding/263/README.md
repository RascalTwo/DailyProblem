# Valid Sentence Checker

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

- The sentence must start with a capital letter, followed by a lowercase letter or a space.
- All other characters must be lowercase letters, separators `(,,;,:)` or terminal marks `(.,?,!,‽)`.
- There must be a single space between each word.
- The sentence must end with a terminal mark immediately following a word.

## Examples

| Input                   | Output  |
| ----------------------- | ------- |
| `'Hello, world!'`       | `True`  |
| `'HEllo, world!'`       | `False` |
| `' A'`                  | `False` |
| `'1 '`                  | `False` |
| `'a bird.'`             | `False` |
| `'A bird.'`             | `True`  |
| `'A bird'`              | `False` |
| `'A bird that flies.'`  | `False` |
| `'A bird; that flies.'` | `True`  |
