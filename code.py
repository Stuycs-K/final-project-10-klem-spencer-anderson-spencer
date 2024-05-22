import sys
import math
def hexdump(file):
    f = open(file, "rb")
    tot = ""
    while (byte := f.read(1)):
        num = int.from_bytes(byte, byteorder='little')
        hexnum = hex(num)[2:]
        if(len(hexnum)<2):
            hexnum = "0"*(2-len(hexnum)) + hexnum
        tot +=  hexnum + " "
    print(tot)

def encode(f1, f2, f3):
    text = open(f1, "rb")
    output = open(f3, "wb")
    key = open(f2, "rb")
    key1 =[]
    i = 0
    while (byte := text.read(1)):
        if(byte2 :=key.read(1)):
            num = int.from_bytes(byte, byteorder='little')
            num2 = int.from_bytes(byte2,byteorder='little')
            xor = num ^ num2
            b = xor.to_bytes(1,byteorder='little')
            key1.append(num2)
            output.write(b)
        else:
            num2 = key1[i%len(key1)]
            num = int.from_bytes(byte, byteorder='little')
            xor = num ^ num2
            b = xor.to_bytes(1,byteorder='little')
            i+=1
            output.write(b)
    output.close()
    text.close()
    key.close()

def decode(f1,f2):
    text = open(f1, "rb")
    key = open(f2, "rb")
    key1 =[]
    i = 0
    tot = ""
    while (byte := text.read(1)):
        if(byte2 :=key.read(1)):
            num = int.from_bytes(byte, byteorder='little')
            num2 = int.from_bytes(byte2,byteorder='little')
            xor = num ^ num2
            key1.append(num2)
            tot+= chr(xor)
        else:
            num2 = key1[i%len(key1)]
            num = int.from_bytes(byte, byteorder='little')
            xor = num ^ num2
            i+=1
            tot+= chr(xor)
    print(tot)
    text.close()
    key.close()

if(len(sys.argv)>=2):
    if sys.argv[1] == "-hexdump":
        hexdump(sys.argv[2])
    if(sys.argv[1]=="-encode"):
        encode(sys.argv[2],sys.argv[3],sys.argv[4])
    if(sys.argv[1]=="-decode"):
        decode(sys.argv[2],sys.argv[3])
