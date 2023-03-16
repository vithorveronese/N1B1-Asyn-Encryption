import Helper
import threading


class NumberGenerator:
    def __init__(self):
        self.result = None

    def generateNumber(self):
        # Generate a number here
        self.result = Helper.generatePrime()

    def get_result(self):
        return self.result

def worker(obj):
    """Thread worker function"""
    obj.generateNumber()

pGenerator = NumberGenerator()
# qGenerator = NumberGenerator()

# Create a new thread and start it
threadP = threading.Thread(target=worker, args=(pGenerator,))
# threadQ = threading.Thread(target=worker, args=(qGenerator,))
threadP.start()
# threadQ.start()

# Wait for the thread to finish

# threadQ.join()
        

# q = qGenerator.get_result()

#p = Helper.generatePrime()

print("")
q = Helper.generatePrime()
threadP.join()
p = pGenerator.get_result()
print(p)
print(q)
print("")
n = Helper.generateN(p, q)
totient = Helper.generateTotient(p, q)
e = Helper.generateE(totient)
d = Helper.generateD(e, totient)

originalText = "Fábio Henrique Cabrini"
print("")
print("Original txt => " + originalText)
print("")
cryptedText = pow(int.from_bytes(originalText.encode(), byteorder='big'), e, n)
print("Crypted text => " + cryptedText)
print("")
decryptedText = int.to_bytes(pow(cryptedText, d, n), length=(cryptedText.bit_length() // 8) + 1, byteorder='big').decode()
print("decrypted text => " + decryptedText)

