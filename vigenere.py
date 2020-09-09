def prepare_string(string: str) -> str:
    # deleting non-alphabetic characters and turning to uppercase
    return ''.join(c.upper() for c in string if c.isalpha())

def encrypt(plaintext: str, keyword: str):
    """encrypting text using vigenere encryption"""
    # preparing texts
    plaintext = prepare_string(plaintext)
    keyword = prepare_string(keyword)
    keyword = [ord(x) - 64 for x in keyword]

    encrypted =  ''
    key = 0

    for char in plaintext:
        # If keyword ends go to the begin
        if key == len(keyword): 
            key = 0
        
        # Appending encrypted letter
        encrypted += encrypt_letter(char, keyword[key])

        # Select next key for shifting
        key += 1

    # Return encrypted text or None if there's none
    return encrypted if encrypted != '' else None

def encrypt_letter(char, shift):
    # Return shifted character for encryption
    return chr((ord(char) + shift - 65) % 26 + 65) 

def decrypt(text: str, keyword: str):
    """decrypting text using vigenere decryption knowing they key"""
    # preparing texts
    text = prepare_string(text)
    keyword = prepare_string(keyword)
    keyword = [ord(x) - 64 for x in keyword]

    decrypted =  ''
    key = 0

    for char in text:
        # If keyword ends go to the begin
        if key == len(keyword): 
            key = 0
        
        # Appending decrypted letter
        decrypted += decrypt_letter(char, keyword[key])

        # Select next key for shifting
        key += 1

    # Return decrypted text or None if there's none
    return decrypted if decrypted != '' else None

def decrypt_letter(char, shift):
    # Return back shifted character for decryption
    return chr((ord(char) - shift - 65) % 26 + 65) 
