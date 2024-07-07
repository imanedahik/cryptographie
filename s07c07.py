from Crypto.Cipher import AES
import base64

# Function to decrypt AES-128 ECB encrypted data
def decrypt_aes_ecb(ciphertext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.rstrip(b'\0')  # Remove padding if any

# Read the base64-encoded ciphertext from file
with open('encrypted.txt', 'r') as file:
    base64_ciphertext = file.read().strip()  # Read and strip any extra whitespace

# Decode the base64 ciphertext
ciphertext = base64.b64decode(base64_ciphertext)

# Define the decryption key
key = 'YELLOW SUBMARINE'

# Decrypt the ciphertext
plaintext = decrypt_aes_ecb(ciphertext, key)

# Print the decrypted plaintext
print(plaintext.decode('utf-8'))