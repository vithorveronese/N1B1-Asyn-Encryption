import time
import Helper
import sys

start_time = time.time()

def saveBackup(fileContents, encrypt):
    newName =""
    if (encrypt):
        newName = "encrypt.txt"
    else:
        newName = "decrypt.txt"
    
    backup = open(newName, "w")
    backup.write(fileContents)
    backup.close()

def caesarCipher(oldContent, ed, n):
    newContent = ""
    for char in oldContent:
        asciiNumber = pow(ord(char), ed, n)
        newChar = chr(asciiNumber)
        newContent += newChar
    return newContent
    
p = Helper.generatePrime()
q = Helper.generatePrime()
n = Helper.generateN(p, q)
totient = Helper.generateTotient(p, q)
e = Helper.generateE(totient)
d = Helper.generateD(e, totient)

cryptKey = pow(p,e,n)
saveBackup(str(cryptKey), True)
decryptKey = pow(cryptKey, d, n)
saveBackup(str(decryptKey), False)

originalText = "Fábio Henrique Cabrini"
print("")
print("Original txt => " + originalText)

cryptedText = caesarCipher(originalText, e, n)
print("")
print("Changed txt => " + cryptedText)

decryptedText = caesarCipher(cryptedText, d, n)
print("")
print("decryptedText => " + decryptedText)

