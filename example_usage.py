"""
Example Usage and Testing
Demonstrates all features of the Crypto Toolkit
"""

from crypto import SymmetricEncryption, AsymmetricEncryption, Encoding, Hashing


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def example_symmetric_encryption():
    """Example: Symmetric encryption with AES, DES, 3DES"""
    print_section("1. SYMMETRIC ENCRYPTION")

    # Test data
    plaintext = "Hello, World! This is a secret message."
    key = "MySecretKey12345"

    # AES Encryption
    print("AES Encryption:")
    print(f"  Plaintext: {plaintext}")
    print(f"  Key: {key}")
    aes_ciphertext = SymmetricEncryption.encrypt_aes(plaintext, key)
    print(f"  Ciphertext: {aes_ciphertext[:60]}...")
    aes_decrypted = SymmetricEncryption.decrypt_aes(aes_ciphertext, key)
    print(f"  Decrypted: {aes_decrypted}")
    print(f"  ✓ Match: {plaintext == aes_decrypted}\n")

    # DES Encryption
    print("DES Encryption:")
    print(f"  Plaintext: {plaintext}")
    print(f"  Key: {key}")
    des_ciphertext = SymmetricEncryption.encrypt_des(plaintext, key)
    print(f"  Ciphertext: {des_ciphertext[:60]}...")
    des_decrypted = SymmetricEncryption.decrypt_des(des_ciphertext, key)
    print(f"  Decrypted: {des_decrypted}")
    print(f"  ✓ Match: {plaintext == des_decrypted}\n")

    # 3DES Encryption
    print("3DES Encryption:")
    print(f"  Plaintext: {plaintext}")
    print(f"  Key: {key}")
    des3_ciphertext = SymmetricEncryption.encrypt_3des(plaintext, key)
    print(f"  Ciphertext: {des3_ciphertext[:60]}...")
    des3_decrypted = SymmetricEncryption.decrypt_3des(des3_ciphertext, key)
    print(f"  Decrypted: {des3_decrypted}")
    print(f"  ✓ Match: {plaintext == des3_decrypted}\n")


def example_asymmetric_encryption():
    """Example: RSA encryption and decryption"""
    print_section("2. ASYMMETRIC ENCRYPTION (RSA)")

    # Test data
    plaintext = "Secret Message"

    print("Generating RSA keys (2048-bit)...")
    public_key, private_key = AsymmetricEncryption.generate_rsa_keys(2048)

    print(f"  Public Key: {public_key[:50]}...")
    print(f"  Private Key: {private_key[:50]}...\n")

    # Encryption
    print("RSA Encryption:")
    print(f"  Plaintext: {plaintext}")
    rsa_ciphertext = AsymmetricEncryption.encrypt_rsa(plaintext, public_key)
    print(f"  Ciphertext: {rsa_ciphertext[:60]}...\n")

    # Decryption
    print("RSA Decryption:")
    rsa_decrypted = AsymmetricEncryption.decrypt_rsa(rsa_ciphertext, private_key)
    print(f"  Decrypted: {rsa_decrypted}")
    print(f"  ✓ Match: {plaintext == rsa_decrypted}\n")


def example_encoding():
    """Example: Base64, Hex, and URL encoding"""
    print_section("3. ENCODING/DECODING")

    # Test data
    text = "Hello, Crypto World!"

    # Base64 Encoding
    print("Base64 Encoding:")
    print(f"  Original: {text}")
    b64_encoded = Encoding.encode_base64(text)
    print(f"  Encoded: {b64_encoded}")
    b64_decoded = Encoding.decode_base64(b64_encoded)
    print(f"  Decoded: {b64_decoded}")
    print(f"  ✓ Match: {text == b64_decoded}\n")

    # Hexadecimal Encoding
    print("Hexadecimal Encoding:")
    print(f"  Original: {text}")
    hex_encoded = Encoding.encode_hex(text)
    print(f"  Encoded: {hex_encoded}")
    hex_decoded = Encoding.decode_hex(hex_encoded)
    print(f"  Decoded: {hex_decoded}")
    print(f"  ✓ Match: {text == hex_decoded}\n")

    # URL Encoding
    print("URL Encoding:")
    text_with_spaces = "Hello World & Special Chars!"
    print(f"  Original: {text_with_spaces}")
    url_encoded = Encoding.encode_url(text_with_spaces)
    print(f"  Encoded: {url_encoded}")
    url_decoded = Encoding.decode_url(url_encoded)
    print(f"  Decoded: {url_decoded}")
    print(f"  ✓ Match: {text_with_spaces == url_decoded}\n")


def example_hashing():
    """Example: MD5 and SHA hashing"""
    print_section("4. HASHING")

    # Test data
    text = "Hello, Crypto Toolkit!"

    print("Hash Generation:")
    print(f"  Input: {text}\n")

    # MD5
    md5_hash = Hashing.hash_md5(text)
    print(f"  MD5: {md5_hash}")

    # SHA-1
    sha1_hash = Hashing.hash_sha1(text)
    print(f"  SHA-1: {sha1_hash}")

    # SHA-256
    sha256_hash = Hashing.hash_sha256(text)
    print(f"  SHA-256: {sha256_hash}")

    # SHA-512
    sha512_hash = Hashing.hash_sha512(text)
    print(f"  SHA-512: {sha512_hash[:60]}...\n")

    # Hash verification (same input = same hash)
    print("Hash Verification:")
    text2 = "Hello, Crypto Toolkit!"
    sha256_hash2 = Hashing.hash_sha256(text2)
    print(f"  SHA-256('{text}') == SHA-256('{text2}'): {sha256_hash == sha256_hash2}\n")


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("  CRYPTO TOOLKIT - EXAMPLE USAGE AND TESTING")
    print("="*60)

    try:
        example_symmetric_encryption()
        example_asymmetric_encryption()
        example_encoding()
        example_hashing()

        print_section("TESTING COMPLETE")
        print("✓ All operations completed successfully!")
        print("✓ Run 'python main.py' to launch the GUI application\n")

    except Exception as e:
        print(f"\n✗ Error occurred: {str(e)}\n")


if __name__ == '__main__':
    main()
