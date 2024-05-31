# This document is required.

Images to use

different versions of block chaining 
![Alt text](image.png)

To create the block cipher we used the nonce and a key and tried a playfair cipher but with hex instead of letters. This way we would be able to xor the bytes rather than the letters.

We decided to use the counter method, which includes a counter and a nonce and we made the counter a large prime number so the block key would be very different everytime.  In this cipher, each part of the text is xored with a different key to make it hard to find patterns and to stop repetition of encoding.
