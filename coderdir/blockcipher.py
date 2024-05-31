import sys
import math
key = 0x1092795f32a7329
nonce = 0x4756394e85c73905
IMG = 1
TEXT = 0
MODE = IMG



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
### STEP 4: USE GENERALKEY + BLOCKNUM AND PLAYFAIR TO GET BLOCKKEY
### STEP 5: XOR BLOCKKEY AND CIPHERTEXT
### STEP 6: REPEAT


def nonceIncrement (n, nonce = 123456789123, counter = 4952019383323): 
    return n * counter + nonce


#give plaintext in int form and key in int form
#returns hex array
def playfairEncode (num1, num2):
    colShift = 1
    rowShift = 1
    hexAr = [[0x0, 0x1, 0x2, 0x3],
             [0x4, 0x5, 0x6, 0x7],
             [0x8, 0x9, 0xa, 0xb],
             [0xc, 0xd, 0xe, 0xf]]
    finAr = []
    hex1 = hex(num1)[2:]
    hex2 = hex(num2)[2:]
    pos = 0
    while pos < len(hex1) and pos < len(hex2):
        i = int(hex1[pos], 16)
        j = int(hex2[pos], 16)
        row1 = i % 4
        row2 = j % 4
        col1 = i // 4
        col2 = j // 4

        if row1 == row2 and col1 == col2:
            finAr.append(hexAr[(row1 + rowShift)  % 4][(col1 + colShift)  % 4])
            finAr.append(hexAr[(row2 + rowShift)  % 4][(col2 + colShift)  % 4])
        elif col1 == col2:
            finAr.append(hexAr[(row1 + rowShift)  % 4][col1])
            finAr.append(hexAr[(row2 + rowShift)  % 4][col2])
        elif row1 == row2:
            finAr.append(hexAr[row1][(col1 + colShift)  % 4])
            finAr.append(hexAr[row2][(col2 + colShift)  % 4])
        else:
            finAr.append(hexAr[row1][col1])
            finAr.append(hexAr[row2][col2])
        pos += 1
    
    return finAr


#give int Ar, returns a 2d array, first array inside is
#number, second is key in hex
def playfairDecode (intAr):
    colShift = -1
    rowShift = -1
    hexAr = [[0x0, 0x1, 0x2, 0x3],
             [0x4, 0x5, 0x6, 0x7],
             [0x8, 0x9, 0xa, 0xb],
             [0xc, 0xd, 0xe, 0xf]]
    finAr = [[], []]
    pos = 0
    while pos < len(intAr):
        i = intAr[pos]
        j = intAr[pos + 1]
        row1 = i % 4
        row2 = j % 4
        col1 = i // 4
        col2 = j // 4
        if row1 == row2 and col1 == col2:
            finAr[0].append(hexAr[(row1 + rowShift)  % 4][(col1 + colShift)  % 4])
            finAr[1].append(hexAr[(row2 + rowShift)  % 4][(col2 + colShift)  % 4])
        elif col1 == col2:
            finAr[0].append(hexAr[(row1 + rowShift)  % 4][col1])
            finAr[1].append(hexAr[(row2 + rowShift)  % 4][col2])
        elif row1 == row2:
            finAr[0].append(hexAr[row1][(col1 + colShift)  % 4])
            finAr[1].append(hexAr[row2][(col2 + colShift)  % 4])
        else:
            finAr[0].append(hexAr[row1][col1])
            finAr[1].append(hexAr[row2][col2])    
        pos += 2
    return finAr


def saveHex(arr, filename):
    with open(filename, 'wb+') as f:
        for a in arr:
            f.write(bytes(a,))


def hexdump(filename):
    finStr = ''    
    with open(filename, 'rb+') as f:
        text = f.read()
        for b in text:
            b = b.to_bytes(1, byteorder='little')
            finStr += b.hex() + ' '
    f.close()
    return finStr


def hexEncode(inputTextfile, keyfile, outputCiphertextfile):
    with open(inputTextfile, 'rb+') as f1, open(keyfile, 'rb+') as f2,  open(outputCiphertextfile, 'rb+') as f3:
        text1 = f1.read()        
        text2 = f2.read()
        i = 0
        while (i < len(text1)):
            b1 = text1[i] ^ text2[i % len(text2)]
            f3.write(b1.to_bytes(1, byteorder='little'))
            i += 1
        f3.close

def hexDecode(inputCiphertextfile, keyfile):
    with open(inputCiphertextfile, 'rb+') as f1, open(keyfile, 'rb+') as f2:
        text1 = f1.read()        
        text2 = f2.read()
        i = 0
        finAr = []
        while (i < len(text1)):
            b1 = text1[i] ^ text2[i % len(text2)]
            finAr.append(b1)
            i += 1
    return finAr
def imgEncode(inputTextfile, keyfile, outputCiphertextfile):
    with open(inputTextfile, 'rb+') as f1, open(keyfile, 'rb+') as f2,  open(outputCiphertextfile, 'rb+') as f3:
        text1 = f1.read() 
             
        text2 = f2.read()
        i = 170
        f3.write(text1[0:i])
        while (i < len(text1)):
            b1 = text1[i] ^ text2[i % len(text2)]
            f3.write(b1.to_bytes(1, byteorder='little'))
            i += 1
        
        f3.close

def textToHex(textSeg):
    finStr = ''
    for character in textSeg:
        finStr +=  hex(ord(character))
        
    return finStr
#to be finished

def fullEncode(outputfile, message, key):
    #split text 
    n = 6
    seg = 0
    finHexAr = []
    while seg < len(message):
        pos = seg
        while (pos - seg) < n and pos < len(message):
            encodeNum = int(textToHex(message[pos]), 16)
            hexAr = playfairEncode(encodeNum, nonce)
            nonceIncrement(pos)
            pos += 1

        finHexAr = finHexAr + hexAr
        seg += n


    saveHex(finHexAr, 'input.txt')
    keyNumArr = []
    for character in key:
        keyNumArr.append(int(textToHex(character), 16))
    saveHex(keyNumArr, 'key.txt')
    hexEncode('input.txt', 'key.txt', outputfile)

def fullDecode(inputfile, outputfile, key):
    keyNumArr = []
    for character in key:
        keyNumArr.append(int(textToHex(character), 16))
    saveHex(keyNumArr, 'key.txt')
    hexDecode(inputfile, 'key.txt', 'input.txt')
    
def runner():
    if sys.argv[1] == 'hexdump':
        print(hexdump(sys.argv[2]))    
    elif sys.argv[1] == 'encode':
        hexEncode(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == 'decode':
        print(hexDecode(sys.argv[2], sys.argv[3]))

def organizer(mode):
    if mode == 'encode':
        pass
    elif mode == 'decode':
        pass

# x = [0x1,0x2,0x3, 0xa, 0xff]
# saveHex(x, "testing")
# print(hexdump("testing"))
text = "hi how are you doing. This is a secret message"
length = 5
#print(splitText(text, length))
#hexEncode("img.jpg","key.txt","output.txt")
#hexEncode("img.jpg","key.txt","output.jpg")
#finar=(hexDecode("output.jpg","key.txt"))
#saveHex(finar, "output.jpg")
#print(playfairDecode(playfairEncode(32, 32)))
fullEncode('output.txt', text, 'histuff')
print(hexdump('output.txt'))