from cryptography.fernet import Fernet
import base64

# Genera una clave y guárdala en un lugar seguro
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message):
    return cipher_suite.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message):
    return cipher_suite.decrypt(encrypted_message.encode()).decode()

# Ejemplo de uso
original_message = "Este es un mensaje secreto"
encrypted_message = encrypt_message(original_message)
decrypted_message = decrypt_message(encrypted_message)

print(f"Original: {original_message}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")