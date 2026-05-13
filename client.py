# Server: Bob

# RSA:
# Get bit_length from user
# Choose p & q
# Calculate n, phi, e, & d
# Make n,e public
# get secrate Key from Alice and decode

#AES (More modern)
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import math
import random

# Miller-Rabin test
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def generate_primes(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # ensure size and odd

        if is_prime(num):
            return num


def RSA_Setup(bit_length):
    #Step 1: Generate primes
    p = generate_primes(bit_length // 2)
    q = generate_primes(bit_length // 2)
    while q == p :
        q = generate_primes(bit_length//2)

    #Step 2: compute n
    n = p*q

    #Step 3: compute phi
    phi = (p-1)*(q-1)

    #Step 4: choose e
    e = 65537

    #Step 5: compute d
    d = pow (e, -1, phi)

    return (n,e,d)
def decrypt_RSA(c,d,n):
    a = pow(c,d,n)
    return a


def AES_Encrypt(message,key):
    key = key.to_bytes(16,'big')
    cipher = AES.new(key,AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv, ciphertext

def AES_Decrypt(iv,cipher,key):
    key = key.to_bytes(16,'big')
    cipher_obj = AES.new(key,AES.MODE_CBC, iv)
    message = unpad(cipher_obj.decrypt(cipher), AES.block_size)
    return message.decode()

def main():
    #RSA Set up
    bit_length = int(input("Please enter bit lenght: "))
    n,e,d = RSA_Setup(bit_length)
    print ("Public Keys(n,e):",n,e)
    #print ("Private Keys(d):", d )
    print(" ")

    #RSA Decryption
    c = int(input("Please enter secret key cipher: "))
    key = decrypt_RSA(c,d,n)
    print ("Secrete key: ",key)
    print (" ")
    #AES CHAT
    ans = ""
    while ans != "quit":
        # AES Decryption
        ans = input("Would you like to decrypt a message (Y/N): ")
        print(" ")
        if ans == "Y":
            iv = bytes.fromhex(input("Enter IV (hex): "))
            cipher = bytes.fromhex(input("Please enter cipher here: "))
            message = AES_Decrypt(iv, cipher,key)
            print ("Message: ", message)
            print(" ")

        ans = input("Would you like to encrypt a message (Y/N): ")
        if ans == "Y":
            message = input("Please enter message here: ")
            iv, cipher = AES_Encrypt(message,key)
            print("IV: ", iv.hex())
            print("Cipher: ",cipher.hex())
            print(" ")

        ans = input("If you are done please enter the word 'quit', otherwise enter go: ")
        print(" ")
main()