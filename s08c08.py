
ciphertexts = [
    "6bc1bee22e409f96e93d7e117393172a",
    "6bc1bee22e409f96e93d7e117393172a",  
    "6bc1bee22e409f96e93d7e117393172a",
    "6bc1bee22e409f96e93d7e117393172a"
]

def detect_aes_ecb(ciphertext):
    blocks = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]
    return len(blocks) != len(set(blocks))
index = 1
while index <= len(ciphertexts):
    if detect_aes_ecb(ciphertexts[index - 1].strip()):
        print(f"ECB mode detected in ciphertext {index}")
    else:
        print(f"No ECB mode detected in ciphertext {index}")
    index += 1
