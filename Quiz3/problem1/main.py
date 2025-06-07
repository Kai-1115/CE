# Problem1-Question3
import hashlib
import os

def derive_key(password: str, salt: bytes, key_length: int = 32) -> bytes:
    shake = hashlib.shake_128()
    shake.update(password.encode() + salt)
    return shake.digest(key_length)

def generate_keystream(key: bytes, length: int) -> bytes:
    shake = hashlib.shake_128()
    shake.update(key)
    return shake.digest(length)

def encrypt(plaintext: str, password: str) -> tuple:
    salt = os.urandom(16)
    key = derive_key(password, salt) # derive the key
    print("Key: ", key)
    keystream = generate_keystream(key, len(plaintext)) # generate a keystream
    
    ciphertext = bytes([p ^ k for p, k in zip(plaintext.encode(), keystream)]) # transform into ciphertext
    
    return salt, ciphertext 

def decrypt(salt: bytes, ciphertext: bytes, password: str) -> str:
    key = derive_key(password, salt)
    keystream = generate_keystream(key, len(ciphertext))
    
    plaintext = bytes([c ^ k for c, k in zip(ciphertext, keystream)])
    
    return plaintext.decode()

password = "securepassword"
message = input("Input the plaintext: ")

salt, encrypted = encrypt(message, password)
print("Encrypted:", encrypted.hex())

decrypted = decrypt(salt, encrypted, password)
print("Decrypted:", decrypted)
