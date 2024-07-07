def repeating_key_xor(plaintext, key):
    ciphertext = []
    key_len = len(key)
    for i in range(len(plaintext)):
        xor_byte = ord(plaintext[i]) ^ ord(key[i % key_len])
        ciphertext.append(xor_byte)
    return ''.join(format(byte, '02x') for byte in ciphertext)

plaintext = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

ciphertext = repeating_key_xor(plaintext, key)
print(ciphertext)
