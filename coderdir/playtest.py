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

#print(playfairEncode(ord("C"), ord("y")))
print(playfairDecode(playfairEncode(ord("a"), ord("y"))))
#print(hex(ord('a')),hex(ord('y')))