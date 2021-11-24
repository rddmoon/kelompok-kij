import sdes
from sdes import *

def MAC(k, m):
    counter = 0
    index = 0
    textToProcess = ""
    for i in m:
        i = ord(i) #setiap karakter diubah jadi unicode
        if (counter == 0):
            i = encrypt(k, i) #i dienkripsi menggunakan k
            counter = 1
            textToProcess += chr(i) #ngumpulin karakter yang diubah jadi string lagi
            #print(textToProcess)
        else:
            i = i ^ ord(textToProcess[index-1]) 
            i = encrypt(k, i)
            textToProcess += chr(i)
        index += 1
    

    for i in textToProcess: 
        if (not isinstance(i, str)): #mastiin bahwa tiap i di texttoprocess itu unicode
            i = chr(i) #ngubah ke string

    return textToProcess

def enkrip_message_internal(key, message):
    F = MAC(key, message)
    F = message + '||' + F
    #print("testing f internal",F)
    textToProcess = ""
    for i in F:
        i = ord(i)
        i = encrypt(key, i)
        textToProcess += chr(i)
   #print("testing en_internal",textToProcess)
    return textToProcess

def dekrip_message_internal(key, cipher):
    textToProcess = ""
    valid = False
    F = ""

    for i in cipher:
        i = ord(i)
        i = decrypt(key, i)
        textToProcess += chr(i)
    
    M = textToProcess.split("||") [0]
    F = textToProcess.split("||") [1]

   # print("pengentau M :" , M) #ngecek M value nya apa 
  #  print("Pengentau F:" , F) #ngecek F value nya apa
 #   print("Pengetau mac m:", MAC(key,M)) #ngecek M setelah dienkripsi pake Mac function

    #validasi/mastiin hasi enkripsi M dengan mac function sama dengan F
    if MAC(key, M) == F:
      valid = True
    
    return M, valid

def enkrip_message_external(key, message):
    textToProcess = ""
    for i in message:
        i = ord(i)
        i = encrypt(key, i)
        textToProcess += chr(i)
    #print(textToProcess)
    F = MAC(key, textToProcess)
    F = textToProcess + '||' + F
    #print (F)
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