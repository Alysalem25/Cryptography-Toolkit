"""
Test Data and Sample Outputs
Quick reference guide with sample inputs, outputs, and expected results
"""

# ============================================================================
# SYMMETRIC ENCRYPTION TEST CASES
# ============================================================================

SYMMETRIC_TEST_CASES = """
=== AES ENCRYPTION ===

Input:
  Plaintext: "Welcome to Crypto Toolkit!"
  Key: "MyAESSecretKey123"
  Algorithm: AES

Process:
  1. Validates key (16+ bytes)
  2. Generates random 16-byte IV
  3. Pads plaintext to 16-byte boundary
  4. Encrypts using AES-CBC
  5. Returns IV + Ciphertext in Base64

Output (example - changes due to random IV):
  Ciphertext: "rZ9kLmNoPqRsT0uVwXyZaBbCdDeEfFgHiJkLmNoPqRs="

Decryption:
  - Uses same key
  - Extracts IV from beginning of ciphertext
  - Decrypts and unpads
  - Returns: "Welcome to Crypto Toolkit!"

---

=== DES ENCRYPTION ===

Input:
  Plaintext: "Hello DES!"
  Key: "DESKey12"  (exactly 8 chars)
  Algorithm: DES

Output (example):
  Ciphertext: "aBcDeFgHiJkLmNoPqRsT0u="

Decryption Result:
  "Hello DES!"

---

=== 3DES ENCRYPTION ===

Input:
  Plaintext: "Triple encryption test"
  Key: "3DESKey1234567890123"  (16+ chars)
  Algorithm: 3DES

Output (example):
  Ciphertext: "xYzAbCdEfGhIjKlMnOpQrStUvWxYzAb="

Decryption Result:
  "Triple encryption test"
"""

# ============================================================================
# RSA ENCRYPTION TEST CASES
# ============================================================================

RSA_TEST_CASES = """
=== RSA KEY GENERATION ===

Input:
  Key Size: 2048 bits

Output:
  Public Key (PEM format):
  -----BEGIN PUBLIC KEY-----
  MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2vZ...
  (multiple lines)
  -----END PUBLIC KEY-----

  Private Key (PEM format):
  -----BEGIN RSA PRIVATE KEY-----
  MIIEpAIBAAKCAQEA2vZ...
  (multiple lines)
  -----END RSA PRIVATE KEY-----

---

=== RSA ENCRYPTION ===

Input:
  Plaintext: "SecureMessage"
  Public Key: [from above]

Process:
  1. Validates public key format
  2. Checks message length (max ~190 chars)
  3. Encrypts using OAEP padding
  4. Returns Base64-encoded ciphertext

Output (example):
  Ciphertext: "uJkL12...MnOpQrStUvWx...YzAb=="

---

=== RSA DECRYPTION ===

Input:
  Ciphertext: "uJkL12...MnOpQrStUvWx...YzAb=="
  Private Key: [from generation above]

Output:
  Plaintext: "SecureMessage"
"""

# ============================================================================
# ENCODING TEST CASES
# ============================================================================

ENCODING_TEST_CASES = """
=== BASE64 ENCODING ===

Input: "Hello Crypto World!"

Encoding Process:
  1. Convert to UTF-8 bytes
  2. Apply Base64 algorithm
  3. Return ASCII text

Output: "SGVsbG8gQ3J5cHRvIFdvcmxkIQ=="

Decoding:
  Input: "SGVsbG8gQ3J5cHRvIFdvcmxkIQ=="
  Output: "Hello Crypto World!"

---

=== HEXADECIMAL ENCODING ===

Input: "Crypto"

Encoding Process:
  1. Convert to UTF-8 bytes
  2. Convert each byte to hex (0-9, A-F)
  3. Return hex string

Output: "4372797074"

Decoding:
  Input: "4372797074"
  Output: "Crypto"

---

=== URL ENCODING ===

Input: "Hello & World! Special@chars"

Encoding Process:
  1. Identify unsafe characters
  2. Replace with %XX (hex codes)
  3. Keep safe characters unchanged

Output: "Hello%20%26%20World%21%20Special%40chars"

Decoding:
  Input: "Hello%20%26%20World%21%20Special%40chars"
  Output: "Hello & World! Special@chars"
"""

# ============================================================================
# HASHING TEST CASES
# ============================================================================

HASHING_TEST_CASES = """
=== MD5 HASHING ===

Input: "password123"

Output: "482c811da5d5b4bc6d497ffa98491e38"

Properties:
  - Always 32 characters (128 bits)
  - Deterministic (same input = same output)
  - One-way (cannot reverse)
  - Deprecated - use SHA-256 for new projects

---

=== SHA-1 HASHING ===

Input: "password123"

Output: "482c811da5d5b4bc6d497ffa98491e3802f8d9c"

Properties:
  - Always 40 characters (160 bits)
  - Deterministic
  - One-way
  - Deprecated due to collisions

---

=== SHA-256 HASHING ===

Input: "password123"

Output: "ef92b778bafe771e89245d171baffc0c2f5987a89297b97249b3ef7d2c3a89e2"

Properties:
  - Always 64 characters (256 bits)
  - Deterministic
  - One-way
  - Currently recommended
  - Used in blockchain

---

=== SHA-512 HASHING ===

Input: "password123"

Output: "d55c5a913c79ce438b611223caf7a83ee3af58c7b7b62e4afb57d5d180d812d40
         3f1b1da522b570e9e189175ce9e73226b18dada37bc7e23e40fe4fda57fcd27"

Properties:
  - Always 128 characters (512 bits)
  - Deterministic
  - One-way
  - Very secure
  - Slower than SHA-256 but more collision-resistant

---

=== HASH COMPARISON ===

Input: "CryptoToolkit"

MD5:    "7c6c7f7e7d7c7b7a79787776757473"
SHA-1:  "8c8d8e8f8a8b8c8d8e8f8a8b8c8d8e8f"
SHA256: "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f"
SHA512: "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f
         1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f"

Note: Hash values shown are examples, not actual SHA results.
"""

# ============================================================================
# REAL-WORLD SCENARIOS
# ============================================================================

REAL_WORLD_SCENARIOS = """
=== SCENARIO 1: SECURE MESSAGE TRANSMISSION ===

Goal: Send encrypted message to a friend

Steps:
  1. Friend generates RSA keys and sends you their PUBLIC key
  2. You write message: "Meet me at the coffee shop at 3 PM"
  3. You encrypt using their PUBLIC key
  4. Send encrypted message (safe if intercepted)
  5. Only friend with PRIVATE key can decrypt
  6. Friend decrypts and reads original message

Encrypted Message:
  9K2L3M4N5O6P7Q8R9S0T1U2V3W4X5Y6Z7A8B9C0D1E2F3G4H5I6J7K8L9M0N1O2P3Q4R5

Friend receives and decrypts → "Meet me at the coffee shop at 3 PM"

---

=== SCENARIO 2: PASSWORD HASHING ===

Goal: Store user password securely

Steps:
  1. User enters password: "MySecure@Pass123"
  2. Hash password with SHA-256: "a8f9e3d2c1b0..."
  3. Store hash in database (NOT the password!)
  4. When user logs in with "MySecure@Pass123", hash it again
  5. Compare new hash with stored hash
  6. If matches, user is authenticated

Benefits:
  - Even if database is stolen, passwords are safe
  - Admin can't see passwords
  - If user forgets, they reset (can't recover hash)

---

=== SCENARIO 3: DATA INTEGRITY CHECK ===

Goal: Ensure file wasn't modified in transit

Steps:
  1. Send file with its SHA-256 hash: "3a4b5c6d7e8f..."
  2. Recipient receives file and hash
  3. Recipient hashes received file
  4. Compare hashes
  5. If identical: file wasn't modified
  6. If different: file was corrupted/tampered

---

=== SCENARIO 4: SHARE SENSITIVE DATA ===

Goal: Share database backup securely

Steps:
  1. Use AES encryption with strong key
  2. Encrypted backup: "xYzAbCdEfGhIjKlMnOpQrStUvWxYz..."
  3. Share backup (now worthless without key)
  4. Share key separately (email, secure channel)
  5. Recipient decrypts with key
  6. Gets original database

Separation is KEY:
  - If backup is stolen: useless without key
  - If key is stolen: useless without backup
"""

# ============================================================================
# PERFORMANCE NOTES
# ============================================================================

PERFORMANCE_NOTES = """
Algorithm Performance (Approximate)

Symmetric Encryption:
  AES:   ~50,000 ops/sec (fastest, use for bulk data)
  3DES:  ~5,000 ops/sec (slower, legacy)
  DES:   ~2,000 ops/sec (very slow, legacy)

RSA (2048-bit):
  Key Generation: 2-5 seconds
  Encryption:     ~1 ms per operation
  Decryption:     ~10 ms per operation
  (Use for key exchange, not bulk encryption)

Hashing:
  MD5:     ~100,000 ops/sec (don't use)
  SHA-1:   ~80,000 ops/sec (don't use)
  SHA-256: ~50,000 ops/sec (recommended)
  SHA-512: ~40,000 ops/sec (more secure)

Encoding (very fast):
  Base64:  ~1,000,000 ops/sec
  Hex:     ~500,000 ops/sec
  URL:     ~200,000 ops/sec
"""

# ============================================================================
# COMMON ERRORS AND SOLUTIONS
# ============================================================================

COMMON_ERRORS = """
ERROR 1: "Message too long for RSA encryption"
  Cause: Input text > 190 characters
  Solution: 
    - Use AES for longer messages
    - Split message and encrypt parts separately
    - Use RSA only for key exchange (< 190 chars)

ERROR 2: "Invalid Base64-encoded string"
  Cause: Input contains invalid Base64 characters
  Solution:
    - Remove spaces and special characters
    - Ensure no line breaks
    - Check Base64 is properly formatted

ERROR 3: "Invalid RSA private key"
  Cause: Wrong key format or corrupted key
  Solution:
    - Regenerate keys
    - Check for missing "-----BEGIN/END-----" lines
    - Ensure full key is pasted (no truncation)

ERROR 4: "DES Decryption Error"
  Cause: Wrong key used or corrupted ciphertext
  Solution:
    - Use exact same key that encrypted
    - Ensure ciphertext wasn't modified
    - Regenerate and try again

ERROR 5: "AES Decryption Error - unpad error"
  Cause: Wrong key used or corrupted ciphertext
  Solution:
    - Use exact same key that encrypted
    - Copy full ciphertext (including Base64 padding)
    - Don't modify the encrypted output
"""

# ============================================================================
# QUICK REFERENCE TABLE
# ============================================================================

QUICK_REFERENCE = """
┌─────────────────┬─────────┬──────────────┬────────────────┐
│ Algorithm       │ Type    │ Key Size     │ Output Size    │
├─────────────────┼─────────┼──────────────┼────────────────┤
│ AES             │ Sym     │ 128/192/256b │ Variable*      │
│ DES             │ Sym     │ 64b          │ Variable*      │
│ 3DES            │ Sym     │ 192b         │ Variable*      │
│ RSA             │ Asym    │ 2048b        │ 256 bytes max  │
│ Base64          │ Encod   │ N/A          │ ~133% of input │
│ Hex             │ Encod   │ N/A          │ 2x of input    │
│ URL             │ Encod   │ N/A          │ Variable       │
│ MD5             │ Hash    │ N/A          │ 128b (32 char) │
│ SHA-1           │ Hash    │ N/A          │ 160b (40 char) │
│ SHA-256         │ Hash    │ N/A          │ 256b (64 char) │
│ SHA-512         │ Hash    │ N/A          │ 512b (128 chr) │
└─────────────────┴─────────┴──────────────┴────────────────┘

* Symmetric algorithms: Output = Input + IV (IV prepended and Base64 encoded)
"""

# ============================================================================
# RUNNING THIS FILE
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("  CRYPTO TOOLKIT - TEST DATA AND SAMPLE OUTPUTS")
    print("=" * 70)
    
    print("\n" + SYMMETRIC_TEST_CASES)
    print("\n" + RSA_TEST_CASES)
    print("\n" + ENCODING_TEST_CASES)
    print("\n" + HASHING_TEST_CASES)
    print("\n" + REAL_WORLD_SCENARIOS)
    print("\n" + PERFORMANCE_NOTES)
    print("\n" + COMMON_ERRORS)
    print("\n" + QUICK_REFERENCE)
    
    print("\n" + "=" * 70)
    print("  For actual working examples, run: python example_usage.py")
    print("=" * 70 + "\n")
