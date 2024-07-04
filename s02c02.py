def fixed_xor(buffer1, buffer2):
    # Ensure the buffers are of equal length
    if len(buffer1) != len(buffer2):
        raise ValueError("Buffers must be of equal length")
    # XOR each pair of bytes and store the result in a new buffer
    xor_result = bytes([b1 ^ b2 for b1, b2 in zip(buffer1, buffer2)])

    return xor_result

# Example usage
buffer1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
buffer2 = bytes.fromhex('686974207468652062756c6c277320657965')
xor_result = fixed_xor(buffer1, buffer2)
print(xor_result.hex())  
