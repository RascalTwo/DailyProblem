# Ternary Search Tree

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A ternary search tree is a trie-like data structure where each node may have up to three children.

Here is an example which represents the words `code`, `cob`, `be`, `ax`, `war`, and `we`.

           c
        /  |  \
       b   o   w
     / |   |   |
    a  e   d   a
    |    / |   | \
    x   b  e   r  e

The tree is structured according to the following rules:

- Left child nodes link to words lexicographically earlier than the parent prefix
- Right child nodes link to words lexicographically later than the parent prefix
- Middle child nodes continue the current word

For instance, since `code` is the first word inserted in the tree, and `cob` lexicographically precedes `cod`, `cob` is represented as a left child extending from `cod`.

Implement insertion and search functions for a ternary search tree.
