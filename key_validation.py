from random import randint

def prime(n):
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

def egcd(p, q):
    """Finding the greatest common divisor of p and q"""
    if p == 0:
        return q, 0, 1
    else:
        i, j, k = egcd(q % p, p)
        return i, k - (q // p) * j, j

def modular_inverse(p, q):
    """Applying modular inversion utilising egcd"""
    i, j, k = egcd(p, q)
    if i != 1:
        return """"Public key and private key have no greatest
    common divisor"""
    else:
        return j % q

def validateDecryptionKey(p, q, e, d):
    f = (p-1)*(q-1)
    k = e * d

    while k >= 0:
        k = k - f
        if k == f + 1 or k == f - 1:
            print("Decryption Key: %d is valid" % (d))
            return True

def validateEncryptionKey(p, q, e):
    f = (p-1)*(q-1)
    k = e
    while f != 0:
        try:
            f = f % k
            if f == 1 or k == 1:
                print("Encryption Key: %d is valid" % (e))
                return True            
            k = k % f
        except Exception:
            return None

def validatedKeys():        
    keys_list = []
    for i in range(0, 100):    
        rand = randint(1, 10000)    
        if len(keys_list) < 2:
            if prime(rand) == True:
                keys_list.append(rand)

    print("Public key P: %d is valid" % (keys_list[0]))
    print("Public key Q: %d is valid" % (keys_list[1]))

    for i in range(0, 500):
        r = randint(1, 500)
        if validateEncryptionKey(keys_list[0], keys_list[1], r) == True:
            keys_list.append(r)
            break

    for i in range(0, 10000000):
        try:
            if validateDecryptionKey(keys_list[0], keys_list[1], keys_list[2], i) == True:
                keys_list.append(i)
                break
        except Exception:
            return "No valid decryption key found within range"

    return keys_list

print(validatedKeys())

