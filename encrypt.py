import os
from cryptography.fernet import Fernet
import base64
import hashlib
import pwinput

def derive_key(password):
    # Derive a 32-byte key from the password
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Ask the user to input a password with masked input
password = pwinput.pwinput(prompt="Enter a password to encrypt the file: ", mask='●')

# Derive the key from the user-provided password
key = derive_key(password)

# Initialize Fernet with the derived key
fernet = Fernet(key)

# Ask the user to input the path of the text file to encrypt
file_path = input("Enter the path of the text file to encrypt: ").strip('"')

# Read the contents of the text file
try:
    with open(file_path, 'rb') as file:
        original = file.read()

    # Encrypt the file
    encrypted = fernet.encrypt(original)

    # Ensure the output directory exists
    output_dir = 'encrypted'
    os.makedirs(output_dir, exist_ok=True)

    # Generate output filename with "_encrypted.txt" suffix
    base_filename = os.path.basename(file_path)
    name, ext = os.path.splitext(base_filename)
    encrypted_file_path = os.path.join(output_dir, f"{name}_encrypted.txt")

    # Write the encrypted content to a new file
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"File encrypted successfully and saved as {encrypted_file_path}!")

except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")