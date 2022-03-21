[_metadata_:generated]: - "true"

# Safen User Input Part I - htmlspecialchars

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56bcaedfcf6b7f2125001118`](https://www.codewars.com/kata/56bcaedfcf6b7f2125001118) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Safen User Input Part I - htmlspecialchars

You are a(n) novice/average/experienced/professional/world-famous Web Developer (choose one) who owns a(n) simple/clean/slick/beautiful/complicated/professional/business website (choose one or more) which contains form fields so visitors can send emails or leave a comment on your website with ease.  However, **with ease comes danger**.  Every now and then, a hacker visits your website and attempts to compromise it through the use of **XSS (Cross Site Scripting)**.  This is done by injecting ```script``` tags into the website through form fields which may contain malicious code (e.g. a redirection to a malicious website that steals personal information).

## Mission

Your mission is to implement a function that converts the following potentially harmful characters:

1. ```<``` --> ```&lt;```
2. ```>``` --> ```&gt;```
3. ```"``` --> ```&quot;```
4. ```&``` --> ```&amp;```

Good luck :D

## Extension

If you are an experienced programmer, try shortening your code as much as possible and optimise it to minimise run time.  Experienced programmers should be able to complete this exercise in one line of code.
