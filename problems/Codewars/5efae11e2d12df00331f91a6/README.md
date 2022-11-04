[_metadata_:generated]: - "true"

# Crack the PIN

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5efae11e2d12df00331f91a6`](https://www.codewars.com/kata/5efae11e2d12df00331f91a6) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given is a md5 hash of a five digits long PIN. It is given as string.
Md5 is a function to hash your password:
"password123" ===> "482c811da5d5b4bc6d497ffa98491e38"

Why is this useful?
Hash functions like md5 can create a hash from string in a short time and it is impossible to find out the password, if you only got the hash. The only way is cracking it, means try every combination, hash it and compare it with the hash you want to crack. (There are also other ways of attacking md5 but that's another story)
Every Website and OS is storing their passwords as hashes, so if a hacker gets access to the database, he can do nothing, as long the password is safe enough.

<a href="https://en.wikipedia.org/wiki/Hash_function#:~:text=A%20hash%20function%20is%20any,table%20called%20a%20hash%20table." target="_blank">What is a hash?</a>

<a href="https://en.wikipedia.org/wiki/MD5" target="_blank">What is md5?</a>

Note: Many languages have build in tools to hash md5. If not, you can write your own md5 function or google for an example.

<a href="https://www.codewars.com/kata/password-hashes" target="_blank">Here</a> is another kata on generating md5 hashes!


Your task is to return the cracked PIN as string.

This is a little fun kata, to show you, how weak PINs are and how important a bruteforce protection is, if you create your own login.

If you liked this kata, <a href="https://www.codewars.com/kata/59146f7b4670ba520900000a" target="_blank">here</a> is an extension with short passwords!

Some of my other katas:
<br>
<a href="https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e" target="_blank">Error Correction #1 - Hamming Code</a>
<br>
<a href="https://www.codewars.com/kata/5f0795c6e45bc600247ab794" target="_blank">Hack the NSA</a>
<br>
<a href="https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f" target="_blank">Decode the QR-Code</a>



