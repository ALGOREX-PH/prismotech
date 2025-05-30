def generate_keys():
    return {"public_key": "BGN_PUBLIC", "private_key": "BGN_PRIVATE"}

def encrypt(data, public_key):
    return f"encrypted({data}) with {public_key}"

def decrypt(ciphertext, private_key):
    return f"decrypted({ciphertext}) with {private_key}"