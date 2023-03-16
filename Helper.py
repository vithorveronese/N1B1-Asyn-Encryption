import math
import secrets

def isPrime(n, k=40):
    """
    Miller-Rabin primality test.
    """
    if n % 2 == 0:
        return False

    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generatePrime():
    """
    Generates a random prime number with 2048 bits.
    """
    while True:
        n = secrets.randbits(4096)
        if n % 2 == 0:
            n += 1
        if isPrime(n):
            return n
        
def generateE(phi_n):
    """
    Generates a random integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1.
    """
    while True:
        e = secrets.randbelow(phi_n - 1) + 1
        if math.gcd(e, phi_n) == 1:
            return e
        
   
def generateD(e, totient):
    return pow(e, -1, totient)

def generateTotient(p, q):
    return (p-1)*(q-1)

def generateN(p, q):
    return p * q
