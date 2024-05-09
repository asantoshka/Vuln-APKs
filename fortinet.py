from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_aes(hex_str, key):
    # Convert the hex string back to bytes
    ct = bytes.fromhex(hex_str)
    iv = bytes([117, 122, 39, 67, 114, 124, 115, 44, 113, 116, 124, 123, 58, 89, 118, 94])
    key = key.encode() 
    
    # Create AES cipher instance
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    
    # Decrypt and unpad the result
    decrypted_data = unpad(aes.decrypt(ct), AES.block_size)
    
    return decrypted_data.decode('utf-8') 

# Example usage
hex_str = "A8A336ACFA6F5BF257C25D669A9EEFFC"
key = "FoRtInEt!AnDrOiD"
try:
    decrypted_text = decrypt_aes(hex_str, key)
    print("Decrypted text:", decrypted_text)
except Exception as e:
    print("Decryption failed:", str(e))