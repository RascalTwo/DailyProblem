[_metadata_:generated]: - "true"

# Condensentences

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5966fb8bccb55fb44b000e51`](https://www.codewars.com/kata/5966fb8bccb55fb44b000e51) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this kata you must condense a given string.

Condensing a string means removing all spaces, and then also removing any extra characters while making sure that all words of the orignal string, are still contained in the same order. This is possible because words can *overlap* in the compressed string, allowing it to be much shorter. Consider the following examples:
```
condense("fat tat attack")
+ fat
+   tat
+    attack
= fatattack 

condense("pugs so cool")
+ pugs
+    so
+      cool
= pugsocool

condense("ladder adders")
+ ladder
+  adders
= ladders
```

The function must work with numbers, words that can't be condensed and empty strings as well.

The credit for this algorithm goes to a youtuber by the name of The Daily Programmer.



