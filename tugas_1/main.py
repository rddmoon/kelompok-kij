import random 
import sdes
from sdes import *

# Rumus triple DES 2 keys 
# Cipher text = E(Key1, D(Key2, E(Key1, Plaintext)))
# Plain Text = D(Key1, E(Key2, D(Key1, Chipertext)))

# Triple DES with 3 Keys

# Rumus triple DES 3 keys 
# Cipher text = E(Key3, D(Key2, E(Key1, Plaintext)))
# Plain Text = D(Key1, E(Key2, D(Key3, Chipertext)))

def encrypt_3DES_2key(key1, key2, plaintext):
    """Encrypt plaintext with given key"""
    enkrip_key1 = encrypt(ord(key1), ord(plaintext))
    dekrip_key2 = decrypt(ord(key2), enkrip_key1)
    enkrip_key1 = encrypt(ord(key1), dekrip_key2)    
    current_text = chr(enkrip_key1)
    return current_text


def decrypt_3DES_2key(key1, key2, ciphertext):
    """Decrypt ciphertext with given key"""
    dekrip_key1 = decrypt(ord(key1), ord(ciphertext))
    enkrip_key2 = encrypt(ord(key2), dekrip_key1)
    dekrip_key1 = decrypt(ord(key1), enkrip_key2)    
    current_text = chr(dekrip_key1)
    return current_text

def tripleDES2key(key1, key2, plaintext):
    print("========= Hasil Triple DES dengan 2 keys =========")
    print ("J  | K   | R ")
    print("-------------")
    for i in plaintext:
      enkrip_cipher_text = encrypt_3DES_2key(key1, key2, i)
      dekrip_cipher_text = decrypt_3DES_2key(key1, key2, enkrip_cipher_text)
      print(i, " | ", enkrip_cipher_text, " | ", dekrip_cipher_text)
      print("-------------")
    print('\n')
    
def tripleDES_3key_encrypt(key1, key2, key3, plaintext):
    enkripsi_key1 = encrypt(ord(key1), ord(plaintext)) # Enkripsi (Key1, Plaintext)
    dekripsi_key2 = decrypt(ord(key2), enkripsi_key1) # Dekripsi hasil dari enkripsi diatas
    enkripsi_key3 = encrypt(ord(key3), dekripsi_key2) # Enkripsi hasil dari dekripsi diatas   
    # ord untuk mengubah string menjadi unicode/ascii
    
    cipher_teks = chr(enkripsi_key3) # Hasil Enkripsi menggunakan 3 keys, berupa cipher text, chr untuk mengubah unicode menjadi string
    return cipher_teks

def tripleDES_3key_decrypt(key1, key2, key3, plaintext):
    """Decrypt ciphertext with given key"""
    dekripsi_key3 = decrypt(ord(key3), ord(plaintext)) # Dekripsi hasil cipherteks menggunakan key 3
    enkripsi_key2 = encrypt(ord(key2), dekripsi_key3) # Enkripsi hasil dekripsi diatas
    dekripsi_key1 = decrypt(ord(key1), enkripsi_key2) # Dekripsi hasil enkripsi diatas
    
    plain_teks = chr(dekripsi_key1)
    return plain_teks # Hasil dekripsi ciphertext, kembali ke plaintext

def tripleDES3key(key1, key2, key3, plaintext):
    print("========= Hasil Triple DES dengan 3 keys =========")
    print ("P  |  C  | D ")
    print("-------------")
    for karakter in plaintext: # untuk setiap huruf dari plaintext
      encrypted_cipher_text = tripleDES_3key_encrypt(key1, key2, key3, karakter) #lakukan enkripsi menggunakan 3 keys
      decrypted_cipher_text = tripleDES_3key_decrypt(key1, key2, key3, encrypted_cipher_text) # lakukan dekripsi dari hasil enkripsi tsb
      print(karakter, " | ", encrypted_cipher_text, " | ", decrypted_cipher_text)
      print("-------------")
    print('\n')


# CTR
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
    key1 = "A"
    key2 = "B"
    key3 = "B"
    plainText = "KIJ B"
    counter = random.randrange(256)
    a = ctr_encrypt(k, counter, plainText)
    b = ctr_decrypt(k, counter, a)
    tripleDES2key(key1, key2, plainText)
    tripleDES3key(key1, key2, key3, plainText)

    print("=========== CTR ===========")
    print('Plaintext: ', plainText)
    print('Encrypt: ', a)
    print('Decrypt: ', b)
