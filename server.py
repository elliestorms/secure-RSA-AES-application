# Client:
# RSA
# Use n & e to encrypt secrete key
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import math
import random
def RSA_encrypt(n,e):
    #Step 1: pick secrete key to exchange
    key = random.randint(2,n-1)
    print("Original Key:",key)

    #Step2: Encrypt key
    c = pow(key,e,n)

    return c, key

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
    #RSA
    n = int (input("Please enter public keys n: "))
    e = int (input("Please enter public key e: "))
    print(" ")

    c, key= RSA_encrypt(n,e)
    print ("Encrypted Key: ", c)

    #AES CHAT
    ans = ""
    while ans != "quit":
        # AES Decryption
        ans = input("Would you like to decrypt a message (Y/N): ")
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
        ans = input("If you are done please enter the word 'quit', otherwist type go: ")
        print(" ")
main()