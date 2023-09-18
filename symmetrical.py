import cryptography
from cryptography.fernet import Fernet



def read_key():
    with open("../encryption_keys/sql_master_key.txt") as f:
        lines = f.readlines()

    key = bytes(lines[0], 'utf-8')
    return key


def encrypt(message, key):
    cursor = Fernet(key)
    encrypted_message = cursor.encrypt(message.encode())
    return encrypted_message




def decrypt(message, key):
    cursor = Fernet(key)
    decrypted_message = cursor.decrypt(message).decode()
    return decrypted_message

# key=read_key()
# x=encrypt('hello', key)
# print(x)
# print(decrypt(x, key))

