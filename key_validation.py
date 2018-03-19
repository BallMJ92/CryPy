def validateDecryptionKey(p, q, e, d):
    f = (p-1)*(q-1)
    k = e*d

    while k>=0:
        k = k-f
        if k == f+1 or k== f-1:
            print("Decryption Key: %d is valid\n" % (d))
            print("Valid key values -\nP: %d\nQ: %d\nEncryption Key: %d\nDecryption Key: %d\n" % (p, q, e, d))
            return None


def validateEncryptionKey(p, q, e):
    f = (p-1)*(q-1)
    k = e
    while f!=0:
        try:
            f = f%k
            if f==1 or k==1:
                print("Encryption Key: %d is valid" % (e))
                return None            
            k = k%f
        except Exception:
            return None
        
"""for i in range(1, 1000):
    validateDecryptionKey(77, 31, 7, i)"""

for i in range(0, 20):
    validateEncryptionKey(13, 17, i)
