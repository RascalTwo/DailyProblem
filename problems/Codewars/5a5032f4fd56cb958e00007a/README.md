[_metadata_:generated]: - "true"

# TV Remote

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a5032f4fd56cb958e00007a`](https://www.codewars.com/kata/5a5032f4fd56cb958e00007a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Background

My TV remote control has arrow buttons and an `OK` button.

I can use these to move a "cursor" on a logical screen keyboard to type "words"...

The screen "keyboard" layout looks like this

<style>
  #tvkb {
    width : 300px;
    border: 5px solid gray; border-collapse: collapse;
  }
  #tvkb td {
    color : orange;
    background-color : black;
    text-align : right;
    border: 3px solid gray; border-collapse: collapse;
  }
</style>

<table id = "tvkb">
<tr><td>a<td>b<td>c<td>d<td>e<td>1<td>2<td>3</tr>
<tr><td>f<td>g<td>h<td>i<td>j<td>4<td>5<td>6</tr>
<tr><td>k<td>l<td>m<td>n<td>o<td>7<td>8<td>9</tr>
<tr><td>p<td>q<td>r<td>s<td>t<td>.<td>@<td>0</tr>
<tr><td>u<td>v<td>w<td>x<td>y<td>z<td>_<td>/</tr>
</table>

# Kata task

How many button presses on my remote are required to type a given `word`?

## Notes

* The cursor always starts on the letter `a` (top left)
* Remember to also press `OK` to "accept" each character.
* Take a direct route from one character to the next
* The cursor does not wrap (e.g. you cannot leave one edge and reappear on the opposite edge)
* A "word" (for the purpose of this Kata) is any sequence of characters available on my virtual "keyboard" 

# Example

word = `codewars`

* c => `a`-`b`-`c`-OK = 3
* o => `c`-`d`-`e`-`j`-`o`-OK = 5
* d => `o`-`j`-`e`-`d`-OK = 4
* e => `d`-`e`-OK = 2
* w => `e`-`j`-`o`-`t`-`y`-`x`-`w`-OK = 7
* a => `w`-`r`-`m`-`h`-`c`-`b`-`a`-OK = 7
* r => `a`-`f`-`k`-`p`-`q`-`r`-OK = 6
* s => `r`-`s`-OK = 2

Answer = 3 + 5 + 4 + 2 + 7 + 7 + 6 + 2 = 36

<hr style="background-color:orange;height:2px;width:75%;margin-top:30px;margin-bottom:30px;"/>

<span style="color:orange;">
*Good Luck!<br/>
DM.*
</span>

<hr>

Series
* TV Remote
* <a href=https://www.codewars.com/kata/tv-remote-shift-and-space>TV Remote (shift and space)
* <a href=https://www.codewars.com/kata/tv-remote-wrap>TV Remote (wrap)</a>
* <a href=https://www.codewars.com/kata/tv-remote-symbols>TV Remote (symbols)</a>
</a>


