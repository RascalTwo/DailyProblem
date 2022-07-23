[_metadata_:generated]: - "true"

# Base Conversion

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`526a569ca578d7e6e300034e`](https://www.codewars.com/kata/526a569ca578d7e6e300034e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this kata you have to implement a base converter, which converts **positive integers** between arbitrary bases / alphabets. Here are some pre-defined alphabets:

```javascript
var Alphabet = {
  BINARY:        '01',
  OCTAL:         '01234567',
  DECIMAL:       '0123456789',
  HEXA_DECIMAL:  '0123456789abcdef',
  ALPHA_LOWER:   'abcdefghijklmnopqrstuvwxyz',
  ALPHA_UPPER:   'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  ALPHA:         'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
  ALPHA_NUMERIC: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
};
```
```csharp
public class Alphabet
{
   public const string BINARY = "01";
   public const string OCTAL = "01234567";
   public const string DECIMAL = "0123456789";
   public const string HEXA_DECIMAL = "0123456789abcdef";
   public const string ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz";
   public const string ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
   public const string ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
   public const string ALPHA_NUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
}
```
```python
bin      = '01'
oct      = '01234567'
dec      = '0123456789'
hex      = '0123456789abcdef'
allow    = 'abcdefghijklmnopqrstuvwxyz'
allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
```
```ruby
bin      = '01'
oct      = '01234567'
dec      = '0123456789'
hex      = '0123456789abcdef'
allow    = 'abcdefghijklmnopqrstuvwxyz'
allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
```
```haskell
newtype Alphabet = Alphabet { getDigits :: [Char] } deriving (Show)
bin, oct, dec, hex, alphaLower, alphaUpper, alpha, alphaNumeric :: Alphabet
bin = Alphabet $ "01"
oct = Alphabet $ ['0'..'7']
dec = Alphabet $ ['0'..'9']
hex = Alphabet $ ['0'..'9'] ++ ['a'..'f']
alphaLower    = Alphabet $ ['a'..'z']
alphaUpper    = Alphabet $ ['A'..'Z']
alpha         = Alphabet $ ['a'..'z'] ++ ['A'..'Z']
alphaNumeric  = Alphabet $ ['0'..'9'] ++ ['a'..'z'] ++ ['A'..'Z']
```
```c
const char * bin = "01";
const char * oct = "01234567";
const char * dec = "0123456789";
const char * hex = "0123456789abcdef";
const char * allow = "abcdefghijklmnopqrstuvwxyz";
const char * alup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const char * alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
const char * alnum = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
```

The function `convert()` should take an input (string), the source alphabet (string) and the target alphabet (string). You can assume that the input value always consists of characters from the source alphabet. You don't need to validate it.

### Examples

```javascript
// convert between numeral systems
convert("15", Alphabet.DECIMAL, Alphabet.BINARY); // should return "1111"
convert("15", Alphabet.DECIMAL, Alphabet.OCTAL); // should return "17"
convert("1010", Alphabet.BINARY, Alphabet.DECIMAL); // should return "10"
convert("1010", Alphabet.BINARY, Alphabet.HEXA_DECIMAL); // should return "a"

// other bases
convert("0", Alphabet.DECIMAL, Alphabet.ALPHA); // should return "a"
convert("27", Alphabet.DECIMAL, Alphabet.ALPHA_LOWER); // should return "bb"
convert("hello", Alphabet.ALPHA_LOWER, Alphabet.HEXA_DECIMAL); // should return "320048"
convert("SAME", Alphabet.ALPHA_UPPER, Alphabet.ALPHA_UPPER); // should return "SAME"
```
```csharp
// convert between numeral systems
Convert("15", Alphabet.DECIMAL, Alphabet.BINARY); // should return "1111"
Convert("15", Alphabet.DECIMAL, Alphabet.OCTAL); // should return "17"
Convert("1010", Alphabet.BINARY, Alphabet.DECIMAL); // should return "10"
Convert("1010", Alphabet.BINARY, Alphabet.HEXA_DECIMAL); // should return "a"

// other bases
Convert("0", Alphabet.DECIMAL, Alphabet.ALPHA); // should return "a"
Convert("27", Alphabet.DECIMAL, Alphabet.ALPHA_LOWER); // should return "bb"
Convert("hello", Alphabet.ALPHA_LOWER, Alphabet.HEXA_DECIMAL); // should return "320048"
Convert("SAME", Alphabet.ALPHA_UPPER, Alphabet.ALPHA_UPPER); // should return "SAME"
```
```python
convert("15", dec, bin)       ==>  "1111"
convert("15", dec, oct)       ==>  "17"
convert("1010", bin, dec)     ==>  "10"
convert("1010", bin, hex)     ==>  "a"
convert("0", dec, alpha)      ==>  "a"
convert("27", dec, allow)     ==>  "bb"
convert("hello", allow, hex)  ==>  "320048"
```
```ruby
convert("15", dec, bin)   # should return "1111"
convert("15", dec, oct)   # should return "17"
convert("1010", bin, dec) # should return "10"
convert("1010", bin, hex) # should return "a"
convert("0", dec, alpha)  # should return "a"
convert("27", dec, allow) # should return "bb"
convert("hello", allow, hex) # should return "320048"
```
```haskell
convert dec bin "15"   `shouldBe` "1111"
convert dec oct "15"   `shouldBe` "17"
convert bin dec "1010" `shouldBe` "10"
convert bin hex "1010" `shouldBe` "a"
convert dec alpha      "0"     `shouldBe` "a"
convert dec alphaLower "27"    `shouldBe` "bb"
convert alphaLower hex "hello" `shouldBe` "320048"
```
```c
convert("15", dec, bin)       // should return "1111"
convert("15", dec, oct)       // should return "17"
convert("1010", bin, dec)     // should return "10"
convert("1010", bin, hex)     // should return "a"
convert("0", dec, alpha)      // should return "a"
convert("27", dec, allow)     // should return "bb"
convert("hello", allow, hex)  // should return "320048"
```

Additional Notes:

* The maximum input value can always be encoded in a number without loss of precision in JavaScript. In Haskell, intermediate results will probably be too large for `Int`.
* The function must work for any arbitrary alphabets, not only the pre-defined ones
* You don't have to consider negative numbers
