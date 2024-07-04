import binascii
import base64

def hex_to_base64(hex_str):
    # Convert hex string to bytes
    bytes_data = binascii.unhexlify(hex_str)
    
    # Convert bytes to base64 encoded string
    base64_data = base64.b64encode(bytes_data)
    
    # Convert bytes to string
    return base64_data.decode()

# Example usage
hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
base64_str = hex_to_base64(hex_str)
print(base64_str)  
