### Counter (CTR) Cipher

Hello, this is Spencer and Spencer back for another let's play


In class we learned about basic 
Here are some different versions of block chaining 
![Alt text](image.png)

We decided to use the counter method, which includes a counter and a nonce and we made the counter a large prime number so the block key would be very different everytime.  In this cipher, each part of the text is xored with a different key to make it hard to find patterns and to stop repetition of encoding.


To create the block cipher we used the nonce and a key and tried a playfair cipher but with hex instead of letters. This way we would be able to xor the bytes rather than the letters.

This allows us to encode any type of document being text, images, and more.

An example of what could happen if the key doesn't change everytime is this ECB Linux Penguin
![alt text](image2.png)

In this case, because the key was so short, it was repeated over and over and ended up encoding the image in a predicable manner. 

Different keys could cause different colors like this:

![alt text](img.png)

But either way this didn't do a good job of encoding the image.

We didn't implement the encoding for images, but it would be easy to adjust it, reading the bytes of the input file rather than the text.



### Implementation of Hex PlayFair:

We learned about typical playfairs, 5 by 5 grids with letters where one letter has to be excluded (typically i or j replace each other)


![alt text](playfair.png)


The plaintext would be broken into pairs and there were certain rules to generate the new pairs from the pairs of letters. 

What we did instead was to create pairs using a number from the key turned into integers and a nonce that would be changed throughout the encoding.

Then we had a 4 by 4 playfair that went from 0 to 15 and could be changed for further levels of encoding.

These would create a pair of numbers, so the key would always become twice as long when put through the playfair, making it more secure.





