import sys
import math
key = 10927958327329
nonce = 47563948573905


###### ENCODER
### STEP 0: SPLIT PLAINTEXT INTO BLOCKS
### STEP 1: NONCE, COUNTER
### STEP 2: COMBINE INTO BLOCKNUM
### STEP 3: 4x4 HEX PLAYFAIR
### STEP 4: USE GENERALKEY + BLOCKNUM AND PLAYFAIR TO GET BLOCKKEY
### STEP 5: XOR BLOCKKEY AND PLAINTEXT
### STEP 6: REPEAT 


###### DECODER
### STEP 0: SPLIT CIPHERTEXT INTO BLOCKS
### STEP 1: NONCE, COUNTER

### STEP 2: COMBINE INTO BLOCKNUM
### STEP 3: 4x4 HEX PLAYFAIR

#no worky
def splitText(text, length):
    sects = math.ceil(len(text)/length)
    i = 0
    finArray = []
    while( i<sects):
        print("hi") #no worky



def hexplayfair (num1, num2):
    hexAr = [[0x0, 0x1, 0x2, 0x3],
             [0x4, 0x5, 0x6, 0x7],
             [0x8, 0x9, 0xa, 0xb],
             [0xc, 0xd, 0xe, 0xf]]
    finAr = []
    hex1 = hex(num1)[2:]
    hex2 = hex(num2)[2:]
    pos = 0
    while pos < len(hex1):
        i = int(hex1[pos], 16)
        j = int(hex2[pos], 16)
        finAr.append(hexAr[i % 4][j / 4])
        finAr.append(hexAr[j % 4][i / 4])
        pos += 1
    
    return finAr
    pass

def saveHex(arr, filename):
    with open(filename, 'wb+') as f:
        for a in arr:
            f.write(bytes((a,)))



### STEP 4: USE GENERALKEY + BLOCKNUM AND PLAYFAIR TO GET BLOCKKEY
### STEP 5: XOR BLOCKKEY AND CIPHERTEXT
### STEP 6: REPEAT 
def hexdump(filename):
    finStr = ''
    with open(filename, 'rb+') as f:
        text = f.read()
        for b in text:
            b = b.to_bytes(1, byteorder='little')
            finStr += b.hex() + ' '
    f.close()
    return finStr

def encode(inputTextfile, keyfile, outputCiphertextfile):
    with open(inputTextfile, 'rb+') as f1, open(keyfile, 'rb+') as f2,  open(outputCiphertextfile, 'rb+') as f3:
        text1 = f1.read()        
        text2 = f2.read()
        i = 0
        while (i < len(text1)):
            b1 = text1[i] ^ text2[i % len(text2)]
            f3.write(b1.to_bytes(1, byteorder='little'))
            i += 1
        f3.close

def decode(inputCiphertextfile, keyfile):
    with open(inputCiphertextfile, 'rb+') as f1, open(keyfile, 'rb+') as f2:
        text1 = f1.read()        
        text2 = f2.read()
        i = 0
        finStr = ''
        while (i < len(text1)):
            b1 = text1[i] ^ text2[i % len(text2)]
            finStr +=chr(b1)
            i += 1
    return finStr

def runner():
    if sys.argv[1] == 'hexdump':
        print(hexdump(sys.argv[2]))    
    elif sys.argv[1] == 'encode':
        encode(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == 'decode':
        print(decode(sys.argv[2], sys.argv[3]))


#runner()

hexplayfair(32, 32)
# x = [0x1,0x2,0x3, 0xa, 0xff]
# saveHex(x, "testing")
# print(hexdump("testing"))
