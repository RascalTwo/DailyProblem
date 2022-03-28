[_metadata_:generated]: - "true"

# Aspect Ratio Cropping - Part 1

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`596e4ef7b61e25981200009f`](https://www.codewars.com/kata/596e4ef7b61e25981200009f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The aspect ratio of an image describes the proportional relationship between its width and its height. Most video shown on the internet uses a 16:9 aspect ratio, which means that for every pixel in the Y, there are roughly 1.77 pixels in the X (where 1.77 ~= 16/9). As an example, 1080p video with an aspect ratio of 16:9 would have an X resolution of 1920, however 1080p video with an aspect ratio of 4:3 would have an X resolution of 1440.

Write a function that accepts arbitrary X and Y resolutions and converts them into resolutions with a 16:9 aspect ratio that maintain equal height. Round your answers up to the nearest integer.

This kata is part of a series with <a href="https://www.codewars.com/kata/aspect-ratio-cropping-part-2">Aspect Ratio Cropping - Part 2</a> .

<h1>Example</h1>
<i>374 × 280 pixel image with a 4:3 aspect ratio.</i>

<a title="By thewikipedian, uploaded by Andreas -horn- Hornig (Photo by thewikipedian.) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3AAspect_ratio_4_3_example.jpg"><img width="256" alt="Aspect ratio 4 3 example" src="https://upload.wikimedia.org/wikipedia/commons/4/43/Aspect_ratio_4_3_example.jpg"/></a>


<i>500 × 280 pixel image with a 16:9 aspect ratio.</i>

<a title="By thewikipedian, uploaded by Benedicto16 (Photo by thewikipedian.) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC-BY-SA-3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3AAspect_ratio_16_9_example3.jpg"><img width="256" alt="Aspect ratio 16 9 example3" src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Aspect_ratio_16_9_example3.jpg"/></a>
