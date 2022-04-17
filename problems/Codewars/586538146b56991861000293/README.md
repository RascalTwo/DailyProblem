[_metadata_:generated]: - "true"

# If you can read this...

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`586538146b56991861000293`](https://www.codewars.com/kata/586538146b56991861000293) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The idea for this kata came from 9gag today:

[![The lyrics to "Never gonna give you up" by Rick Astley encoded in the NATO phonetic alphabet](https://9gag.com/photo/amrb4r9_700b.jpg)](http://9gag.com/gag/amrb4r9)

## Task 

You'll have to translate a string to Pilot's alphabet ([NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)).

**Input:**

`If, you can read?`

**Output:**

`India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?`

**Note:**

* There are preloaded dictionary you can use, named `NATO`
* The set of used punctuation is `,.!?`.
* Punctuation should be kept in your return string, but spaces should not.
* __Xray__ should not have a dash within.
* Every word and punctuation mark should be seperated by a space ' '.
* There should be no trailing whitespace

~~~if:php
<span style="color:red">Although the proper alphabet for j is </span>`Juliett`<span style="color:red"> you have to use </span>`Juliet`<span style="color:red"> here</span>
~~~

~~~if:rust
The NATO phonetic alphabet (A–Z) is preloaded:

```rust
use preloaded::NATO;

NATO[&'R']; // Romeo
NATO[&'U']; // Uniform
NATO[&'S']; // Sierra
NATO[&'T']; // Tango
```

<details>
<summary>Click to see the preloaded code</summary>

```rust
use std::collections::HashMap;
use once_cell::sync::Lazy;

#[rustfmt::skip]
pub static NATO: Lazy<HashMap<char, &'static str>> = Lazy::new(|| {
    [
        ('A', "Alfa"), ('B', "Bravo"), ('C', "Charlie"), ('D', "Delta"),
        ('E', "Echo"), ('F', "Foxtrot"), ('G', "Golf"), ('H', "Hotel"),
        ('I', "India"), ('J', "Juliett"), ('K', "Kilo"), ('L', "Lima"),
        ('M', "Mike"), ('N', "November"), ('O', "Oscar"), ('P', "Papa"),
        ('Q', "Quebec"), ('R', "Romeo"), ('S', "Sierra"), ('T', "Tango"),
        ('U', "Uniform"), ('V', "Victor"), ('W', "Whiskey"), ('X', "Xray"),
        ('Y', "Yankee"), ('Z', "Zulu"),
    ]
    .iter()
    .copied()
    .collect()       
});
```

</details>
~~~
