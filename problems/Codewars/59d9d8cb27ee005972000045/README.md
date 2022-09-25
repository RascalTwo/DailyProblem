[_metadata_:generated]: - "true"

# Catalog

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59d9d8cb27ee005972000045`](https://www.codewars.com/kata/59d9d8cb27ee005972000045) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You are given a *small* extract of a catalog:

```
s = "<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>

<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>

<prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>

<prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>

<prod><name>saw</name><prx>9</prx><qty>10</qty></prod>

...
```

(`prx` stands for `price`, `qty` for `quantity`) and an article i.e "saw".

The `function catalog(s, "saw")` returns the line(s) corresponding to the article
with `$` before the prices:

```
"table saw > prx: $1099.99 qty: 5\nsaw > prx: $9 qty: 10\n..."
```

If the article is not in the catalog return "Nothing".

#### Notes
- There is a blank line between two lines of the catalog.

- The same article may appear more than once. If that happens return all the lines concerned by the article (in the same order as in the catalog; however see below a note for Prolog language).

- The line separator of results may depend on the language `\n`or `\r\n`.
  In **Pascal** `\n` is replaced by `LineEnding`.

- in Perl use "£" instead of "$" before the prices.

-  You can see examples in the "Sample tests".

#### Note for Prolog language
- If the article is not in the catalog then R equals "".

- R substrings (separated by "\n") must be in alphabetic order.

