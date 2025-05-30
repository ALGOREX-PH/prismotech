from prismotech.bgn import encrypt, decrypt

def test_encrypt_decrypt():
    encrypted = encrypt("hello", "BGN_PUBLIC")
    decrypted = decrypt(encrypted, "BGN_PRIVATE")
    assert "decrypted" in decrypted