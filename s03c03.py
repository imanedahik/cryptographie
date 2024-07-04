def single_byte_xor(data, key):
    return bytes([b ^ key for b in data])

# Example usage:
plaintext = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
key = 42  # The key can be any byte (0-255)

# Encrypt
ciphertext = single_byte_xor(plaintext, key)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt (using the same key)
decrypted = single_byte_xor(ciphertext, key)
print("Decrypted text:", decrypted.decode())
