import secrets

def generate_crypto_salt(length=16):
    return secrets.token_hex(length)

print(f"Generated Salt: {generate_crypto_salt()}")
