# Solve 2-CNF Formula

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A Boolean formula can be said to be satisfiable if there is a way to assign truth values to each variable such that the entire formula evaluates to `True`.

For example, suppose we have the following formula, where the symbol `¬` is used to denote negation:

    (¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)

One way to satisfy this formula would be to let `a = False`, `b = True`, and `c = True`.

This type of formula, with `AND` statements joining tuples containing exactly one `OR`, is known as `2-CNF`.

Given a `2-CNF` formula, find a way to assign truth values to satisfy it, or return `False` if this is impossible.

## Examples

| Input                                                   | Output                                 |
| ------------------------------------------------------- | -------------------------------------- |
| `'(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)'` | `{ 'a': False, 'b': True, 'c': True }` |
| `'a AND b AND ¬a'`                                      | `False`                                |
