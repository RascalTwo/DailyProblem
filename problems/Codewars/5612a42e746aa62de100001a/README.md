[_metadata_:generated]: - "true"

# Decibel Scale

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5612a42e746aa62de100001a`](https://www.codewars.com/kata/5612a42e746aa62de100001a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The following formula is called the Decibel Scale:

![Decibel Scale Formula](http://i.imgur.com/EikMPFO.png)

The Decibel Scale is used to determine the loudness of a sound, measured in dB:

* **β** is the result we want, defined in dB;
* We multiply the result of the logarithmic operation by 10, otherwise it'll be called "Bel Scale";
* We provide **I**, the **intensity** of the sound wave we need to find the loudness of, which is, for the purposes of this Kata, measured in 2D space and, hence, in **Watts per square meter**;
* Finally, we divide the intensity by the **threshold of human hearing**, also measured in **Watts per square meter**. This is the softest possible sound a human ear can hear;
* Since the threshold of human hearing involves an extremely small, long number, we need to utilize a logarithmic operation that will provide us the result in a convenient way.

Your task is to simply calculate the loudness of a sound wave, given its intensity as a parameter to the **dBScale/db_scale** function.

*Results are automatically rounded to the **nearest integer** by the test cases.*

