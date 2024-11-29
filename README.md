# key-turn

A basic Python application for encrypting and decrypting files using a password-based key derived from user input.

## Features

- Encrypts plaintext files using a password.
- Decrypts files using the same password for verification.
- Ensures password security with masked input during entry.
- Saves encrypted and decrypted outputs in designated directories.

## Requirements

- Python 3.x
- `cryptography` library
- `pwinput` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd key-turn
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Encrypt a file:**

   Run `encrypt.py` and follow the prompts to input a password and choose a file to encrypt.

   ```bash
   python encrypt.py
   ```

2. **Decrypt a file:**

   Run `decrypt.py` and follow the prompts to input the correct password and provide the encrypted file's path.

   ```bash
   python decrypt.py
   ```

## File Paths & Output

- The encrypted output is saved in the `encrypted/` directory as `<filename>_encrypted.txt`.
- The decrypted output is saved in the `decrypted/` directory as `<filename>_decrypted.txt`.
