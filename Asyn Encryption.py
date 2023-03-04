import secrets

def is_prime(n, k=40):
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

def generate_prime():
    """
    Generates a random prime number with 2048 bits.
    """
    while True:
        n = secrets.randbits(2048)
        if n % 2 == 0:
            n += 1
        if is_prime(n):
            return n
        
p = generate_prime()
q = generate_prime()