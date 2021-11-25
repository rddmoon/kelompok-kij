import sdes
from sdes import *

def MAC(k, m):
    counter = 0
    index = 0
    MACtext = ""
    for i in m:
        i = ord(i) #setiap karakter diubah jadi unicode
        if (counter == 0):
            i = encrypt(k, i) #i dienkripsi menggunakan k
            counter = 1
            MACtext += chr(i) #ngumpulin karakter yang diubah jadi string lagi
            #print(MACtext)
        else:
            i = i ^ ord(MACtext[index-1])  
            i = encrypt(k, i)
            MACtext += chr(i)
        index += 1

    return MACtext

def enkrip_message_internal(key, message):
    F = MAC(key, message)
    F = message + '||' + F
    #print("testing f internal",F)
    internalText = ""
    for i in F:
        i = ord(i)
        i = encrypt(key, i)
        internalText += chr(i)
   #print("testing en_internal",textToProcess)
    return internalText

def dekrip_message_internal(key, cipher):
    internalText = ""
    valid = False
    F = ""

    for i in cipher:
        i = ord(i)
        i = decrypt(key, i)
        internalText += chr(i)
    
    M = internalText.split("||") [0]
    F = internalText.split("||") [1]

   # print("pengentau M :" , M) #ngecek M value nya apa 
  #  print("Pengentau F:" , F) #ngecek F value nya apa
 #   print("Pengetau mac m:", MAC(key,M)) #ngecek M setelah dienkripsi pake Mac function

    #validasi/mastiin hasi enkripsi M dengan mac function sama dengan F
    if MAC(key, M) == F:
      valid = True
    
    return M, valid

def enkrip_message_external(key, message):
    externalText = ""
    for i in message:
        i = ord(i)
        i = encrypt(key, i)
        externalText += chr(i)
    #print(textToProcess)
    F = MAC(key, externalText)
    F = externalText + '||' + F
    #print (F)
    return F

def dekrip_message_external(key, cipher):
    externalText = ""
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
        externalText += chr(i)
    
    return externalText, valid

if __name__ == '__main__':
    plaintext = "aku terlalu buruk untuk kamu"
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