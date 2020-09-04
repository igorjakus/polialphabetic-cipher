def prepare_string(string):
    """we prepare text to be used in algorithm"""
    # Changing to uppercase
    string = string.upper()

    # Deleting spaces
    while ' ' in string:
        string = string.replace(' ', '')
    
    # Returning corected version
    return string

def encrypt(plaintext: str, key: str) -> str:
    """encrypting text using vigenere encryption"""
    # preparing texts
    plaintext = prepare_string(plaintext)
    key = prepare_string(key)
    key = [ord(x) - 64 for x in key]

    encrypted =  ''
    key_index = 0

    for char in plaintext:
        if key_index == len(key): 
            key_index = 0
        shift = key[key_index]
        encrypted += encrypt_letter(char, shift)
        key_index += 1

    return encrypted

def encrypt_letter(char, shift):
    moved = chr((ord(char) + shift - 64) % 26 + 64) 
    return moved if moved.isalpha() else 'Z'

def decrypt(text: str, key: str) -> str:
    """decrypting text using vigenere decryption"""
    # preparing texts
    text = prepare_string(text)
    key = prepare_string(key)
    key = [ord(x) - 64 for x in key]

    decrypted =  ''
    key_index = 0
        
    for char in text:
        if key_index == len(key): 
            key_index = 0
        shift = key[key_index]
        decrypted += decrypt_letter(char, shift)
        key_index += 1

    return decrypted

def decrypt_letter(char, shift):
    moved = chr((ord(char) - shift - 64) % 26 + 64) 
    return moved if moved.isalpha() else 'Z'
