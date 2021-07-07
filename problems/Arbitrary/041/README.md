[_metadata_:tags]:-        "string"

# 041

Receive a term and return the next term according to the below rules:

A term is defines as the number of repetitions of each digit combined with that digit itself of the previous term.

If the initial term was `2`, the next term would be `12`, as there are `one 2`'s.

The next would be `1112` - `one 1` and `one 2`.

The next 7 terms starting from `2` are as such:

```
12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112
```

> The values should be returned from the generator as strings, not numbers.

***

Bonus: Write a generator that gets the next `n` terms using the method written above.
