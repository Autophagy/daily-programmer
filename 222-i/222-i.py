#This is an implementation of the RC4 stream cipher
#(https://en.wikipedia.org/wiki/RC4#Description)

def RC4(key, data):
    S = range(256)
    S = KSA(S, key)
    output = PRGA(S, data)

    return output

#Key-scheduling algorithm (KSA)
def KSA(S, key):
    j = 0
    for i in range(len(S)):
        k = ord(key[i % len(key)])
        j = (j + S[i] + k) % 256
        S[i], S[j] = S[j], S[i]

    return S

#Psuedo-random generation algorithm (PRGA)
def PRGA(S, data):
    i, j = 0, 0
    output = []
    for character in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]

        output.append(XOR(character,K))
    return output

def XOR(a,b):
    return chr(ord(a)^b)

def encrypt(key, data):
    return ''.join(RC4(str(key), data))

def decrypt(key, ciphertext):
    return ''.join(RC4(str(key), ciphertext))

key = 31337
message = "Attack at dawn"

ciphertext = encrypt(key, message)
plaintext = decrypt(key, ciphertext)

print('Original message: ' + message)
print('Plaintext: ' + plaintext)
