import time
import Helper

start_time = time.time()     

p = Helper.generatePrime()
print("")
print(p)
print("")
q = Helper.generatePrime()
print(q)
print("")

totient = Helper.generateTotient(p, q)
print(totient)
print("")
e = Helper.generateE(totient)
print(e)
print("")
print(e < totient)
d = Helper.generateD(e, totient)
print("")
print(d)
print(d*e%totient)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
