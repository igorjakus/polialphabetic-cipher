import unittest
from vigenere import encrypt, decrypt

class TestVigenereCipher(unittest.TestCase):

    def test_encryption(self):
        key = 'SnAKE'      
        plaintext = 'meet me at elephant lake'
        expected =  'FSFERXOUPQXDILSMZBVJ'
        self.assertEqual(encrypt(plaintext, key), expected)

        key = 'zZz'      
        plaintext = 'A12'
        expected =  'A'
        self.assertEqual(encrypt(plaintext, key), expected)

        key = 'elOnmusk'      
        plaintext = 'tesla'
        expected =  'YQHZN'
        self.assertEqual(encrypt(plaintext, key), expected)

        key = 'peN'      
        plaintext = 'pineapple'
        expected =  'FNBUFDFQS'
        self.assertEqual(encrypt(plaintext, key), expected)

        key = '22222222'      
        plaintext = 'fkfkfkfkkf'
        expected =  None
        self.assertEqual(encrypt(plaintext, key), expected)

        key = 'zwadew'      
        plaintext = '12931995415941045'
        expected =  None
        self.assertEqual(encrypt(plaintext, key), expected)

        key = 'gwYadawrgjSAffaz'      
        plaintext = 'dqw3rtkwjrtlw3tf3w4tffad'
        expected =  'KNVSXLTBYDEXZLXTMCZE'
        self.assertEqual(encrypt(plaintext, key), expected)

    def test_decryption(self):
        
        key = 'snake'
        encrypted = 'FSFERXOUPQXDILSMZBVJ'
        expected =  'MEETMEATELEPHANTLAKE'
        self.assertEqual(decrypt(encrypted, key), expected)

        key = 'gwYadawrgjSAffaz'
        encrypted = 'KNVSXLTBYDEXZLXTMCZE'
        expected =  'DQWRTKWJRTLWTFWTFFAD'
        self.assertEqual(decrypt(encrypted, key), expected)

        key = 'pEn'
        encrypted = 'FNBUFDFQS'
        expected =  'PINEAPPLE'
        self.assertEqual(decrypt(encrypted, key), expected)

        key = 'zZz'      
        encrypted = 'a'
        expected =  'A'
        self.assertEqual(decrypt(encrypted, key), expected)


if __name__ == '__main__':
    unittest.main()
