import Helper
import threading
import time
from Crypto.Util.number import getPrime

numerOfBits = 1000
class NumberGenerator:
    def __init__(self):
        self.result = None

    def generateNumber(self):
        self.result = getPrime(numerOfBits)

    def get_result(self):
        return self.result

def worker(obj):
    """Thread worker function"""
    obj.generateNumber()

def generateKeys():
    pGenerator = NumberGenerator()
    threadP = threading.Thread(target=worker, args=(pGenerator,))
    threadP.start()
    q = getPrime(numerOfBits)
    threadP.join()
    p = pGenerator.get_result()
    n = Helper.generateN(p, q)
    totient = Helper.generateTotient(p, q)
    e = Helper.generateE(totient)
    d = Helper.generateD(e, totient)
    publicKey = (e, n)
    privateKey = (d, n)
    keys = [privateKey, publicKey]
    return keys

def getPrivateKey():
    return privateKey

def getPublicKey():
    return publicKey

def decryptMessage(encryptedText, key):
    return int.to_bytes(pow(encryptedText, key[0], key[1]), length=(encryptedText.bit_length() // 8) + 1, byteorder='big').decode()

def encryptMessage(originalText, key):
    return pow(int.from_bytes(originalText.encode(), byteorder='big'), key[0], key[1])


# originalText = "Fábio Henrique Cabrini"
# print("")
# print("Original txt => " + originalText)
# print("")
# cryptedText = pow(int.from_bytes(originalText.encode(), byteorder='big'), e, n)
# print("Crypted text => ", cryptedText)
# print("")
# decryptedText = int.to_bytes(pow(cryptedText, d, n), length=(cryptedText.bit_length() // 8) + 1, byteorder='big').decode()
# print("decrypted text => " + decryptedText)

