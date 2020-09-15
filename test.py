from vigenere import encrypt, decrypt


def test_encryption_1():
    key = 'snake'
    plaintext = 'meet me at elephant lake '
    expected = 'FSFERXOUPQXDILSMZBVJ'
    assert encrypt(plaintext, key) == expected


def test_encryption_2():
    key = 'abc'
    plaintext = 'cbacbacba'
    expected = 'DDDDDDDDD'
    assert encrypt(plaintext, key) == expected


def test_encryption_none():
    key = ''
    plaintext = 'example'
    expected = None
    assert encrypt(plaintext, key) == expected


def test_decryption_1():
    key = 'snake'
    encrypted = 'FSFERXOUPQXDILSMZBVJ'
    expected = 'MEETMEATELEPHANTLAKE'
    assert decrypt(encrypted, key) == expected


def test_decryption_2():
    key = 'zyx'
    encrypted = 'aaaaaaaaa'
    expected = 'ABCABCABC'
    assert decrypt(encrypted, key) == expected


def test_decryption_none():
    key = 'example'
    encrypted = ''
    expected = None
    assert decrypt(encrypted, key) == expected
