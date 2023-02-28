[_metadata_:generated]: - "true"

# Adding words - Part I

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`592eaf848c91f248ca000012`](https://www.codewars.com/kata/592eaf848c91f248ca000012) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

<p>This is the first part of this kata series. Second part is <a href="https://www.codewars.com/kata/adding-words-part-ii/">here</a> and third part is <a href="https://www.codewars.com/kata/adding-words-part-iii/">here</a></p>
<p>Add two English words together!</p>
<p>Implement a class <code>Arith</code> (struct <code>struct Arith{value : &'static str,}</code> in Rust) such that</p>

```javscript
  //javascript
  var k = new Arith("three");
  k.add("seven"); //this should return "ten" 
```

```c++
  //c++
  Arith* k = new Arith("three");
  k->add("seven"); //this should return string "ten" 
```

```Rust
  //Rust
  let c = Arith{value: "three"};
  c.add("seven") // this should return &str "ten"
```
<p><b>Input</b> - Will be between zero and ten and will always be in lower case</p>
<p><b>Output</b> - Word representation of the result of the addition. Should be in lower case</p>

