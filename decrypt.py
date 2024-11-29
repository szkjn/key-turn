from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib
import pwinput
import os

def derive_key(password):
    # Derive a 32-byte key from the password
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Ask the user to input a password with masked input
password = pwinput.pwinput(prompt="Enter the password to decrypt the file: ", mask='●')

# Derive the key from the user-provided password
key = derive_key(password)

# Initialize Fernet with the derived key
fernet = Fernet(key)

# Ask the user to input the path of the encrypted file
encrypted_file_path = input("Enter the path of the encrypted file: ").strip('"')

# Read the encrypted file
try:
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    # Attempt to decrypt the file
    try:
        decrypted = fernet.decrypt(encrypted)

        # Ensure the output directory exists
        output_dir = 'decrypted'
        os.makedirs(output_dir, exist_ok=True)

        # Determine the output filename
        base_filename = os.path.basename(encrypted_file_path)
        if "_encrypted.txt" in base_filename:
            name, ext = os.path.splitext(base_filename)
            decrypted_filename = name.replace("_encrypted", "_decrypted") + ext
        else:
            name, ext = os.path.splitext(base_filename)
            decrypted_filename = f"{name}_decrypted{ext}"

        decrypted_file_path = os.path.join(output_dir, decrypted_filename)

        # Write the decrypted content to a new file in the output directory
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        print(f"File decrypted successfully and saved as {decrypted_file_path}!")

    except InvalidToken:
        print("Error: The password is incorrect. Decryption failed.")
except FileNotFoundError:
    print(f"Error: The file {encrypted_file_path} does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")