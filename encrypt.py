base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

print("23456" + "     this is the data being encrypted")

def key():
    import random
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    outstr = ""
    outstr = outstr + random.choice(base64) #base64 rotation alpha start
    outstr = outstr + str(random.randrange(1, 7)) #base64 rotation alpha augmentation interval
    outstr = outstr + str(random.randrange(10)) #encrypted output rotation
    return outstr

encryptkey = "010"
print(encryptkey + "       this is the key used to encrypt the data")

def encrypt(num, key):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    outstr = ""
    
    alpha = base64[base64.find(key[0])::int(key[1])] + base64[:base64.find(key[0]):int(key[1])] #make enc alpha from key pair
    for x in str(num): #for each num in outstr 1, find the character in alpha with an index that corr. with num
        outstr = outstr + alpha[int(x)]

    rot = int(key[2]) % len(str(num))
    outstr = outstr[rot:] + outstr[:rot]
    
    return outstr

print(encrypt(23456, encryptkey) + "     this is what the data looks like after being encrypted")
encstr = encrypt(23456, encryptkey)

def decrypt(string, key):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    outstr = ""
    
    counterrot = len(string) - (int(key[2]) % len(string))
    string = string[counterrot:] + string[:counterrot]
    
    alpha = base64[base64.find(key[0])::int(key[1])] + base64[:base64.find(key[0]):int(key[1])]
    for x in string:
        outstr =  outstr + str(alpha.find(x))
        
    return int(outstr)

print(str(decrypt(encstr, encryptkey)) + "     this is what the data looks like after being decrypted")

