import sdes as DES
from Crypto import Random
import math

def cbc_encrypt(k, iv, plaintext):
    res = ""
    before = iv
    for i in plaintext:
        c = ord(i) ^ before
        enc = DES.encrypt(k, c)
        before = enc
        res = res + chr(enc)
    return res

    
def cbc_decrypt(k, iv, plaintext):
    res = ""
    before = iv
    for i in plaintext:
        enc = ord(i)
        c = DES.decrypt(k, enc) ^ before
        before = enc
        res = res + chr(c)
    return res
    

if __name__ == '__main__':
    st = "WAHYUFFFdbcdefgh"
    key = 0b1110001110101001010101010101010010101
    iv = 0b10101010
    print(st)
    res = cbc_encrypt(key, iv, st)
    print(res)
    res2 = cbc_decrypt(key, iv, res)
    print(res2)
