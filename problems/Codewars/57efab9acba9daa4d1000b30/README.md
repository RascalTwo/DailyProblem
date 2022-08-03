[_metadata_:generated]: - "true"

# Slaphead

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57efab9acba9daa4d1000b30`](https://www.codewars.com/kata/57efab9acba9daa4d1000b30) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Being a bald man myself, I know the feeling of needing to keep it clean shaven. Nothing worse that a stray hair waving in the wind. 
 
You will be given a string(x). Clean shaved head is shown as "-" and stray hairs are shown as "/". Your task is to check the head for stray hairs and get rid of them. 

You should return the original string, but with any stray hairs removed. Keep count ot them though, as there is a second element you need to return:

0 hairs --> "Clean!"<br>
1 hair --> "Unicorn!"<br>
2 hairs --> "Homer!"<br>
3-5 hairs --> "Careless!"<br>
\>5 hairs --> "Hobo!"

So for this head: "------/------" you shoud return:<br>

["-------------", "Unicorn"]

