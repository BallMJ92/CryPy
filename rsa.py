from random import randint
import sys

"""Increasing recursion limit to caultulate modular inversion of
large public and private keys up to 2048bit key length"""
sys.setrecursionlimit(1500)

def random_key(size):
    """Generates a random key based on key_space function"""
    rmin = 10**(size-1)
    rmax = (10**size)-1
    return randint(rmin, rmax)*2+1

"""2048 bit encryption == keys of 617 digits length"""
def key_length(bits):
    if bits < 512:
        raise ValueError("Key size too small")
    elif bits == 512:
        return 155
    elif bits == 1024:
        return 309
    elif bits == 2048:
        return 617
    return 617

"""Generates public key"""
def public_key(): return random_key(key_length())

"""Generates private key"""
def private_key(): return random_key(key_length())

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

def encryption_key(p, q):
    """Applying modular inverse function to generate encryption
key based on extended euclidean algorithm"""
    return modular_inverse(p, q) 

def validateDecryptionKey(p, q, e, d):
    """Checks if decryption key is valid for keys p and q, and encryption key e"""
    f = (p-1)*(q-1)
    k = e*d

    while k>=0:
        k = k-f
        if k == f+1 or k== f-1:
            print("Decryption Key: %d is valid\n" % (d))
            print("Valid key values -\nP: %d\nQ: %d\nEncryption Key: %d\nDecryption Key: %d\n" % (p, q, e, d))
            return None

"""Using validateDecryptionKey function to find all valid decryption keys
within specified range"""
for i in range(1, 1000):
    validateDecryptionKey(77, 31, 7, i)
