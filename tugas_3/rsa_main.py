'''
Created on 07.09.2016

@author: Marius

url : https://raw.githubusercontent.com/mx0c/RSA-Implementation-in-Python/master/main.py
'''

import random
import hashlib
max_PrimLength = 1000000000000

'''
calculates the modular inverse from e and phi
'''
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

'''
calculates the gcd of two ints
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
checks if a number is a prime
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generateRandomPrim():
    while(1):
        ranPrime = random.randint(0,max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime

def generate_keyPairs():
    p = generateRandomPrim()
    q = generateRandomPrim()
    
    n = p*q
    # print("n ",n)
    '''phi(n) = phi(p)*phi(q)'''
    phi = (p-1) * (q-1) 
    # print("phi ",phi)
    
    '''choose e coprime to n and 1 > e > phi'''    
    e = random.randint(1, phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
        
    # print("e=",e," ","phi=",phi)
    '''d[1] = modular inverse of e and phi'''
    d = egcd(e, phi)[1]
    
    '''make sure d is positive'''
    d = d % phi
    if(d < 0):
        d += phi
        
    #print("KEYS: ", ((e,n),(d,n)))
    return ((e,n),(d,n))
        
def decrypt(ctext,private_key):
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

def encrypt(text,public_key):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

def hash(data):
    h = hashlib.sha3_256()
    h.update(data)
    st = ""
    for i in h.digest():
        st += str(hex(i)) + "/"
    return st

if __name__ == '__main__':

    # message M dari Alice
    M = b"Hai Bob, aku Alice."

    # Alice generate private key and public key
    public_key, private_key = generate_keyPairs()
    print("Public: ", public_key)
    print("Private: ", private_key)

    # pesan sebagai input hash function menghasilkan hash code
    H = hash(M)

    # hasil digital signature dari enkripsi hash code dan private key pengirim
    signature = encrypt(H, private_key)

    # Alice menggabungkan message dan digital signature lalu dikirim
    dikirim = [M, bytes("||", encoding='UTF-8'), signature]
    print("\nDikirim :")
    print(dikirim)

    # Diterima Bob
    message = dikirim[0]
    signature2 = dikirim[2]

    # pesan yang diterima sebagai input hash function untuk menghasilkan hash code
    H2 = hash(message)

    # Bob dekrip digital signature menggunakan public key Alice
    decrypted = decrypt(signature2, public_key)
    print("\nHash Code\t: " + H)
    print("Decrypted Signature\t: " + decrypted, end="\n\n")

    # jika hash code sama dengan signature yang telah di dekrip, maka VALID
    if (decrypted == H2): print("VALID")


    # plaintext = "Hello World",
    # print("plaintext =", plaintext)
    # ctext = encrypt("Hello World",public_key)
    # print("encrypted  =", ctext)
    # plaintext = decrypt(ctext, private_key)
    # print("decrypted =",plaintext)
