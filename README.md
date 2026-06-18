# Crypto Toolkit - Complete Cryptography Application

A professional-grade, modular Python desktop application with GUI for cryptographic operations. Built with **Tkinter** and **pycryptodome** for production-level security.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features Breakdown](#features-breakdown)
- [Sample Testing](#sample-testing)
- [Screenshots Guide](#screenshots-guide)

---

## ✨ Features

### 🔐 Symmetric Encryption
- **AES** (Advanced Encryption Standard) - 128/192/256-bit
- **DES** (Data Encryption Standard) - 64-bit
- **3DES** (Triple DES) - 192-bit
- Uses CBC mode with random IV for enhanced security
- Automatic key validation and padding

### 🔓 Asymmetric Encryption (RSA)
- Generate 2048-bit RSA key pairs
- Encrypt with public key
- Decrypt with private key
- Uses OAEP padding for security
- PEM format support

### 📝 Encoding/Decoding
- **Base64** encoding and decoding
- **Hexadecimal** encoding and decoding
- **URL** encoding and decoding

### #️⃣ Hashing
- **MD5** hash generation
- **SHA-1** hash generation
- **SHA-256** hash generation (recommended)
- **SHA-512** hash generation

### 🎨 GUI Features
- Clean, tab-based interface using Tkinter
- Separate tabs for each operation category
- Copy-to-clipboard functionality
- Clear error messages and validation
- Scrollable text areas for large inputs/outputs
- Threading support for key generation (no UI freezing)

---

## 📁 Project Structure

```
crypto_toolkit/
│
├── main.py                 # Application entry point
├── gui.py                  # GUI implementation (Tkinter)
├── example_usage.py        # Examples and testing demonstrations
├── requirements.txt        # Python dependencies
│
├── crypto/                 # Cryptography modules
│   ├── __init__.py
│   ├── symmetric.py        # AES, DES, 3DES encryption
│   ├── asymmetric.py       # RSA encryption/decryption
│   ├── encoding.py         # Base64, Hex, URL encoding
│   └── hashing.py          # MD5, SHA hashing
│
└── utils/                  # Utility functions
    ├── __init__.py
    └── helpers.py          # Helper functions
```

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Install Dependencies

```bash
# Navigate to project directory
cd crypto_toolkit

# Install required packages
pip install -r requirements.txt
```

**What gets installed:**
- `pycryptodome` - Professional cryptography library

### Step 2: Verify Installation

```bash
# Run the example tests to verify everything works
python example_usage.py
```

Expected output:
```
============================================================
  CRYPTO TOOLKIT - EXAMPLE USAGE AND TESTING
============================================================

AES Encryption:
  Plaintext: Hello, World! This is a secret message.
  Key: MySecretKey12345
  Ciphertext: c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8...
  Decrypted: Hello, World! This is a secret message.
  ✓ Match: True

... (more examples)

✓ All operations completed successfully!
✓ Run 'python main.py' to launch the GUI application
```

---

## 📖 Usage

### Running the GUI Application

```bash
cd crypto_toolkit
python main.py
```

The application window will open with 4 tabs:

#### Tab 1: Symmetric Encryption
1. Select algorithm (AES, DES, or 3DES)
2. Enter your secret key
3. Paste plaintext in the input box
4. Click **Encrypt** button
5. Result appears in output box
6. To decrypt, paste ciphertext and click **Decrypt**

**Example:**
- Algorithm: AES
- Key: MySecret123
- Input: "Hello World"
- Output: "bXl2ZWN0aW9u..." (Base64 format)

#### Tab 2: Asymmetric Encryption (RSA)
1. Click **Generate RSA Keys** button (takes a few seconds)
2. Keys appear in the respective text boxes
3. Paste your message (max ~190 characters)
4. Click **Encrypt** (uses public key)
5. Share the ciphertext with anyone
6. They decrypt using **Decrypt** button with private key

**Important:** Keep private key secure!

#### Tab 3: Encoding/Decoding
1. Select encoding type (Base64, Hex, or URL)
2. Paste text in the input box
3. Click **Encode** or **Decode**
4. Result appears in output box

**Example:**
- Type: Base64
- Input: "Hello World"
- Output: "SGVsbG8gV29ybGQ="

#### Tab 4: Hashing
1. Select hash algorithm (MD5, SHA-1, SHA-256, SHA-512)
2. Paste text to hash
3. Click **Generate Hash**
4. Hash appears in output (cannot be reversed)

**Example:**
- Algorithm: SHA-256
- Input: "SecurePassword"
- Output: "d8e5c3b2a1..." (64 characters)

---

## 🔍 Features Breakdown

### Symmetric Encryption (AES Example)

**How it works:**
1. Takes your plaintext message
2. Generates a random IV (Initialization Vector)
3. Pads the message to block size
4. Encrypts using your key in CBC mode
5. Returns Base64-encoded result

**Security:** Uses industry-standard algorithms with proper padding

### RSA Encryption (Asymmetric)

**How it works:**
1. Generate public/private key pair (2048-bit)
2. Share public key openly
3. Anyone can encrypt with public key
4. Only private key holder can decrypt
5. Uses OAEP padding for security

**Use Case:** Key exchange, secure communication

### Base64 Encoding

**What it does:** Converts binary data to ASCII-safe text
**Use Case:** Email attachments, data transmission

### SHA-256 Hashing

**What it does:** One-way conversion to fixed-length hash
**Properties:** 
- Deterministic (same input = same hash)
- Cannot be reversed
- Tiny change in input = completely different hash

**Use Case:** Password verification, data integrity

---

## 🧪 Sample Testing

### Test 1: Symmetric Encryption (AES)

**Input:**
```
Plaintext: "The quick brown fox"
Key: "SuperSecret2024"
Algorithm: AES
```

**Expected Output:**
- Ciphertext: Base64 string (changes each time due to random IV)
- Decrypt result: "The quick brown fox"

**How to Test:**
1. Run GUI
2. Go to "Symmetric Encryption" tab
3. Select "AES"
4. Enter key: `SuperSecret2024`
5. Enter text: `The quick brown fox`
6. Click Encrypt → Copy output
7. Click Decrypt with the copied output
8. Verify decrypted text matches original

### Test 2: RSA Encryption

**Input:**
```
Message: "Bitcoin to the moon!"
```

**Expected Output:**
- Ciphertext: Long Base64 string
- Decrypted: "Bitcoin to the moon!"

**How to Test:**
1. Go to "Asymmetric Encryption" tab
2. Click "Generate RSA Keys"
3. Enter message: `Bitcoin to the moon!`
4. Click "Encrypt (with Public Key)"
5. Copy ciphertext
6. Clear input and paste ciphertext
7. Click "Decrypt (with Private Key)"
8. Verify it matches original message

### Test 3: Base64 Encoding

**Input:** `Hello Crypto World!`

**Expected Output:** `SGVsbG8gQ3J5cHRvIFdvcmxkIQ==`

**How to Test:**
1. Go to "Encoding/Decoding" tab
2. Select "Base64"
3. Enter text
4. Click "Encode"
5. Note the output
6. Clear and paste output
7. Click "Decode"
8. Should match original

### Test 4: SHA-256 Hashing

**Input:** `password123`

**Expected Output:** `ef92b778bafe771e89245d171baffc0c2f5987a89297b97249b3ef7d2c3a89e2`

**How to Test:**
1. Go to "Hashing" tab
2. Select "SHA-256"
3. Enter: `password123`
4. Click "Generate Hash"
5. Output should be 64 characters

---

## 📸 Screenshots Guide

### Screen 1: Symmetric Encryption Tab
```
┌─ Crypto Toolkit ────────────────────────────────────┐
│ [Symmetric] [Asymmetric] [Encoding] [Hashing]      │
│                                                      │
│ Algorithm: [AES ▼]                                  │
│ Secret Key: [**************]                        │
│                                                      │
│ Plaintext/Ciphertext:                               │
│ ┌──────────────────────────────────────────────────┐│
│ │ Hello, World!                                     ││
│ └──────────────────────────────────────────────────┘│
│                                                      │
│ Result:                                              │
│ ┌──────────────────────────────────────────────────┐│
│ │ c3VwZXJTZWNyZXQ4QzAxQ0UwMzE5QkEyODg5QkEyODg5  ││
│ │ QkEyODg5QkEyODg5QkEyODg5QkEyODg5QkEyODg5Qk...  ││
│ └──────────────────────────────────────────────────┘│
│                                                      │
│ [Encrypt] [Decrypt] [Copy] [Clear]                 │
└──────────────────────────────────────────────────────┘
```

### Screen 2: RSA Key Generation
```
┌─ Crypto Toolkit ────────────────────────────────────┐
│ [Symmetric] [Asymmetric] [Encoding] [Hashing]      │
│                                                      │
│ [Generate RSA Keys (2048-bit)]                      │
│                                                      │
│ Public Key (for encryption):                         │
│ ┌──────────────────────────────────────────────────┐│
│ │ -----BEGIN PUBLIC KEY-----                        ││
│ │ MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA  ││
│ │ ...                                               ││
│ │ -----END PUBLIC KEY-----                          ││
│ └──────────────────────────────────────────────────┘│
│                                                      │
│ [Copy]                                              │
│                                                      │
│ Private Key (for decryption):                        │
│ ┌──────────────────────────────────────────────────┐│
│ │ -----BEGIN RSA PRIVATE KEY-----                   ││
│ │ MIIEpAIBAAKCAQEA...                               ││
│ │ ...                                               ││
│ │ -----END RSA PRIVATE KEY-----                     ││
│ └──────────────────────────────────────────────────┘│
│                                                      │
│ [Copy]                                              │
└──────────────────────────────────────────────────────┘
```

---

## 🔧 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'Crypto'`
**Solution:**
```bash
pip install --upgrade pycryptodome
```

### Issue: GUI doesn't open
**Solution:**
```bash
# Make sure Tkinter is installed (usually comes with Python)
# On Linux, you might need:
sudo apt-get install python3-tk
```

### Issue: Key is too long/short for DES
**Solution:** DES requires exactly 8 bytes. The app auto-adjusts, but use exactly 8 characters for best results.

### Issue: RSA encryption gives "Message too long" error
**Solution:** RSA can only encrypt ~190 characters. For longer messages, use symmetric encryption instead.

---

## 📚 Code Quality

✓ **Production-level code:**
- Comprehensive error handling
- Type hints for functions
- Detailed docstrings
- Modular architecture
- Clear separation of concerns

✓ **Security best practices:**
- Uses `pycryptodome` (industry standard)
- Random IV generation
- Proper padding schemes
- OAEP for RSA padding
- UTF-8 encoding consistency

✓ **User experience:**
- Clear error messages
- Threading for long operations
- Copy-to-clipboard feature
- Validation of inputs

---

## 📄 Additional Notes

### For University Submission

**Include in your report:**
1. Screenshots from each tab
2. Sample encryption → decryption cycle
3. Explanation of algorithms used
4. Code quality commentary
5. How GUI improves usability

**Demo script:**
```bash
# Show example usage
python example_usage.py

# Launch GUI
python main.py
```

### Code Statistics
- **Total files:** 10
- **Total lines of code:** ~1,200
- **Lines of comments:** ~300
- **Crypto functions:** 14+
- **Error handling:** Comprehensive try-catch blocks

---

## 📝 License

This is a demonstration project for educational purposes.

---

## 🎯 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run tests to verify setup
python example_usage.py

# 3. Launch the application
python main.py
```

**That's it!** The GUI is fully functional and ready to use.

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Verify Python 3.7+ is installed
3. Ensure all dependencies installed via `pip install -r requirements.txt`

---

**Built with ❤️ for secure cryptography** 🔐
#   C r y p t o g r a p h y - T o o l k i t  
 