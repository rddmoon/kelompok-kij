import random
import sdes

def ctr_encrypt(k, counter, plainText):
    cipherText = ""
    for i in plainText:
        x = sdes.encrypt(k, counter)
        i = ord(i) ^ x
        counter += 1
        counter %= 256
        cipherText += chr(i)

    return cipherText

def ctr_decrypt(k, counter, cipherText):
    plainText = ""
    for i in cipherText:
        p = sdes.encrypt(k, counter)
        i = ord(i) ^ p
        counter += 1
        counter %= 256
        plainText += chr(i)

    return plainText

if __name__ == '__main__':
    k = 0b1110001110
    plainText = "Aku CTR"
    counter = random.randrange(256)
    a = ctr_encrypt(k, counter, plainText)
    b = ctr_decrypt(k, counter, a)

    print('Plaintext: ', plainText)
    print('Encrypt: ', a)
    print('Decrypt: ', b)