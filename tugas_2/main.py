import sdes
from sdes import *

def MAC(k, m):
    ctr = 0
    index = 0
    textToProcess = ""
    for i in m:
        i = ord(i)
        if (ctr == 0):
            i = encrypt(k, i)
            ctr = 1
            textToProcess += chr(i)
        else:
            i = i ^ ord(textToProcess[index-1])
            i = encrypt(k, i)
            textToProcess += chr(i)
        index += 1
    
    for i in textToProcess: 
        if (not isinstance(i, str)):
            i = chr(i)

    return textToProcess[11:24]

def enkrip_message_internal(key, message):
    F = MAC(key, message)
    #print(F)
    F = message + '||' + F
    textToProcess = ""
    for i in F:
        i = ord(i)
        i = encrypt(key, i)
        textToProcess += chr(i)
    #print(textToProcess)
    return textToProcess

def dekrip_message_internal(key, cipher):
    textToProcess = ""
    valid = False
    F = ""

    for i in cipher:
        i = ord(i)
        i = decrypt(key, i)
        textToProcess += chr(i)
    
    M = textToProcess.split("||")[0]
    F = textToProcess.split("||")[1]

    #print(M)
    #print(F)

    #validasi
    if MAC(key, M) == F:
      valid = True
    
    return M, valid

def enkrip_message_external(key, message):
    textToProcess = ""
    for i in message:
        i = ord(i)
        i = encrypt(key, i)
        textToProcess += chr(i)
    F = MAC(key, textToProcess)
    F = textToProcess + '||' + F
    return F

def dekrip_message_external(key, cipher):
    textToProcess = ""
    valid = False
    F = ""
    
    M = cipher.split("||")[0]
    F = cipher.split("||")[1]
    
    #validasi
    if MAC(key, M) == F:
       valid = True
       
    for i in M:
        i = ord(i)
        i = decrypt(key, i)
        textToProcess += chr(i)
    
    return textToProcess, valid

if __name__ == '__main__':
    plaintext = "Almamaterku yang kucinta, Ibu yang Luhur ITS"
    key1 = 0b1110001110
    key2 = 0b1110011111
    key3 = 0b1100111100

    cipher_text_internal = enkrip_message_internal(key1, plaintext)
    hasil_internal, valid_internal = dekrip_message_internal(key1, cipher_text_internal)

    print("Hasil Internal : ", hasil_internal)
    print("Validasi Internal : ", valid_internal)

    cipher_text_external = enkrip_message_external(key1, plaintext)
    hasil_external, valid_external = dekrip_message_external(key1, cipher_text_external)

    print("Hasil Eksternal : ", hasil_external)
    print("Validasi Eksternal : ", valid_external)