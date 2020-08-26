def remove_spaces(string):
    while ' ' in string:
        string = string.replace(' ', '')
    return string

def shifts_tab(keyword):
    return [ord(x)-64 for x in keyword]

def encrypt_letter(char, shift):
    moved = chr((ord(char) + shift - 64) % 26 + 64) 
    return moved if moved.isalpha() else 'Z'

def encrypt(text: str, key: str) -> str:
    text = remove_spaces(text.upper())
    key = remove_spaces(key.upper())
    key = shifts_tab(key)

    encrypted =  ''
    key_index = 0
        
    for char in text:
        if key_index == len(key): 
            key_index = 0
        shift = key[key_index]
        encrypted += encrypt_letter(char, shift)
        key_index += 1

    return encrypted

def decrypt_letter(char, shift):
    moved = chr((ord(char) - shift - 64) % 26 + 64) 
    return moved if moved.isalpha() else 'Z'

def decrypt(text: str, key: str) -> str:
    text = remove_spaces(text.upper())
    key = remove_spaces(key.upper())
    key = shifts_tab(key)

    decrypted =  ''
    key_index = 0
        
    for char in text:
        if key_index == len(key): 
            key_index = 0
        shift = key[key_index]
        decrypted += decrypt_letter(char, shift)
        key_index += 1

    return decrypted
    


text = input('Podaj tekst do zaszyfrowania: ')
key = input('Podaj klucz szyfrujący: ')

print('Zaszyfrowany tekst:')
print(encrypt(text, key))

print(' ')

print('Odszyfrowany tekst:')
print(decrypt(encrypt(text, key), key))


