import unittest
from vigenere import encrypt, decrypt

class TestVigenereCipher(unittest.TestCase):

    def test_encryption(self):
        key = ''
        plaintext = ''
        expected =  ''
        actual = encrypt(plaintext, key)
        self.assertEqual(actual, expected)

    def test_decryption(self):
        key = ''
        encrypted = ''
        expected =  ''
        actual = decrypt(encrypted, key)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()