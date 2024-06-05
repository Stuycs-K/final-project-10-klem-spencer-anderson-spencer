import sys
import math
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
def playfairEncode (plainnum, keynum):
    colShift = 1
    rowShift = 1
    hexAr = [[0x0, 0x1, 0x2, 0x3],
             [0x4, 0x5, 0x6, 0x7],
             [0x8, 0x9, 0xa, 0xb],
             [0xc, 0xd, 0xe, 0xf]]
    finAr = []
    plainhex = hex(plainnum)[2:]
    keyhex = hex(keynum)[2:]
    pos = 0
    while pos < len(plainhex) and pos < len(keyhex):

        i = int(plainhex[pos], 16)
        j = int(keyhex[pos], 16)
        row1 = i // 4
        row2 = j // 4
        col1 = i % 4
        col2 = j % 4
        if row1 == row2 and col1 == col2:
            finAr.append(hexAr[(row1 + rowShift)  % 4][(col2 + colShift)  % 4])
            finAr.append(hexAr[(row2 + rowShift)  % 4][(col1 + colShift)  % 4])
        elif col1 == col2:
            finAr.append(hexAr[(row1 + rowShift)  % 4][col2])
            finAr.append(hexAr[(row2 + rowShift)  % 4][col1])
        elif row1 == row2:
            finAr.append(hexAr[row1][(col2 + colShift)  % 4])
            finAr.append(hexAr[row2][(col1 + colShift)  % 4])
        else:
            finAr.append(hexAr[row1][col2])
            finAr.append(hexAr[row2][col1])
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
    finAr = []
    pos = 0
    while pos < len(intAr):
        i = intAr[pos]
        j = intAr[pos + 1]
        row1 = i // 4
        row2 = j // 4
        col1 = i % 4
        col2 = j % 4
        if row1 == row2 and col1 == col2:
            finAr.append(hexAr[(row1 + rowShift)  % 4][(col2 + colShift)  % 4])
        elif col1 == col2:
            finAr.append(hexAr[(row1 + rowShift)  % 4][col2])
        elif row1 == row2:
            finAr.append(hexAr[row1][(col2 + colShift)  % 4])
        else:
            finAr.append(hexAr[row1][col2])
        pos += 2
    return finAr

def saveHex(arr, filename):
    #print(len(arr))
    with open(filename, 'wb+') as f:
        for a in arr:
            #print(a)
            f.write(a.to_bytes(1, byteorder='little'))


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
    with open(inputTextfile, 'rb+') as f1, open(keyfile, 'rb+') as f2,  open(outputCiphertextfile, 'wb+') as f3:
        text1 = f1.read()        
        text2 = f2.read()
        #print(text1, text2)
        i = 0
        while (i < len(text1)):
            b1 = text1[i] ^ text2[i % len(text2)]
            f3.write(b1.to_bytes(1, byteorder='little'))
            i += 1
            #print(b1, i)
        f3.close

def hexDecode(inputCiphertextfile, keyfile):
    with open(inputCiphertextfile, 'rb+') as f1, open(keyfile, 'rb+') as f2:
        text1 = f1.read()        
        text2 = f2.read()
        #print(text2)
        i = 0
        finAr = []
        while (i < len(text1)):
            b1 = text1[i] ^ text2[i % len(text2)]
            finAr.append(b1)
            i += 1
    return finAr



def textToHex(textSeg):
    finStr = ''
    for character in textSeg:
        finStr +=  hex(ord(character))
    return finStr

def fullEncode(outputfile, message, keyfile):
    nonce = 0x4756394e85c73905
    #split text 
    n = 6
    seg = 0
    finHexAr = []
    while seg < len(message):
        pos = seg
        hexAr = []
        while (pos - seg) < n and pos < len(message):
            encodeNum = ord(message[pos])
            hexAr.append(playfairEncode(encodeNum, nonce))
            nonce = nonceIncrement(pos)
            pos += 1
            #print(pos)
        for item in hexAr:
            for item2 in item:
                finHexAr.append(item2)

        #print(len(finHexAr))
        seg += n
    realFinHexAr = []
    pos = 0
    while pos < len(finHexAr):
        realFinHexAr.append(16 * finHexAr[pos] + finHexAr[pos + 1])
        pos += 2
    #print(finHexAr, len(finHexAr))
    #print(finHexAr)
    #print((finHexAr))
    saveHex(realFinHexAr, 'input2.txt')
    #saveHex(key, 'key.txt')
    #print(len(hexdump('input.txt')) // 3)
    hexEncode('input2.txt', keyfile, outputfile)
    #print(len(hexdump('input.txt')) // 3)

def fullDecode(inputfile, outputfile, key):
    #keyNumArr = []
    #for character in key:
    #   keyNumArr.append(ord(character))
    #saveHex(keyNumArr, 'key.txt')
    hexAr = hexDecode(inputfile, 'key.txt')
    #print(hexAr)
    intAr = []
    for item in hexAr:
        intAr.append(item // 16)
        intAr.append(item % 16)
    #print(intAr, len(intAr))
    #finIntAr = playfairDecode(intAr)
    #print(len(intAr))
    finIntAr = playfairDecode(intAr)
    #print(finIntAr, len(finIntAr))
    #nonce = 0x4756394e85c73905
    n = 6
    finStr = ''
    seg = 0
    #print(len(finIntAr))
    while seg < len(finIntAr):
        curChar = chr(finIntAr[seg] * 16 + finIntAr[seg + 1])
        finStr += curChar
        seg += 2
        #print(ord(curChar))
    #print(finStr, len(finStr))
    #print(finHexAr)
    return finStr

def runner():
    if sys.argv[1] == 'hexdump':
        print(hexdump(sys.argv[2]))    
    elif sys.argv[1] == 'encode':
        with open(sys.argv[3],"r") as file:
            text = file.read()
            fullEncode(sys.argv[2],text,sys.argv[4])
            file.close()
        #hexEncode(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == 'decode':
        with open(sys.argv[4],"r") as file:
            text = file.read()
            text2 = fullDecode(sys.argv[2],sys.argv[3],text)
            with open(sys.argv[3], "w") as file2:
                file2.write(text2)
                file2.close()
                
        #print(hexDecode(sys.argv[2], sys.argv[3]))



runner()
