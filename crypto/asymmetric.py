"""
Asymmetric Encryption Module
Handles RSA encryption/decryption and key generation operations.
"""

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class AsymmetricEncryption:
    """
    Handles asymmetric (RSA) encryption operations.
    Supports key generation, encryption, and decryption.
    """

    # Default RSA key size in bits
    DEFAULT_KEY_SIZE = 2048

    @staticmethod
    def generate_rsa_keys(key_size: int = DEFAULT_KEY_SIZE) -> tuple:
        """
        Generate RSA public and private key pair.
        
        Args:
            key_size: Size of the key in bits (default 2048)
            
        Returns:
            Tuple of (public_key_string, private_key_string)
        """
        try:
            # Generate key pair
            key = RSA.generate(key_size)
            
            # Export keys in PEM format
            public_key = key.publickey().export_key().decode('utf-8')
            private_key = key.export_key().decode('utf-8')
            
            return public_key, private_key
        
        except Exception as e:
            raise ValueError(f"RSA Key Generation Error: {str(e)}")

    @staticmethod
    def encrypt_rsa(plaintext: str, public_key_str: str) -> str:
        """
        Encrypt plaintext using RSA public key.
        
        Args:
            plaintext: Text to encrypt
            public_key_str: Public key in PEM format
            
        Returns:
            Base64-encoded ciphertext
        """
        try:
            # Import public key
            public_key = RSA.import_key(public_key_str)
            
            # Create cipher and encrypt
            cipher = PKCS1_OAEP.new(public_key)
            plaintext_bytes = plaintext.encode('utf-8')
            
            # Limit message size (RSA can only encrypt up to key_size - padding)
            # For 2048-bit key, maximum message size is about 190 bytes
            if len(plaintext_bytes) > 190:
                raise ValueError("Message too long for RSA encryption (max ~190 bytes)")
            
            ciphertext = cipher.encrypt(plaintext_bytes)
            
            # Encode to base64 for display/storage
            return base64.b64encode(ciphertext).decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"RSA Encryption Error: {str(e)}")

    @staticmethod
    def decrypt_rsa(ciphertext: str, private_key_str: str) -> str:
        """
        Decrypt RSA-encrypted ciphertext using private key.
        
        Args:
            ciphertext: Base64-encoded ciphertext
            private_key_str: Private key in PEM format
            
        Returns:
            Decrypted plaintext
        """
        try:
            # Import private key
            private_key = RSA.import_key(private_key_str)
            
            # Create cipher and decrypt
            cipher = PKCS1_OAEP.new(private_key)
            ciphertext_bytes = base64.b64decode(ciphertext)
            
            plaintext = cipher.decrypt(ciphertext_bytes)
            
            return plaintext.decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"RSA Decryption Error: {str(e)}")

    @staticmethod
    def verify_public_key(public_key_str: str) -> bool:
        """
        Verify if a string is a valid RSA public key.
        
        Args:
            public_key_str: Public key in PEM format
            
        Returns:
            True if valid, False otherwise
        """
        try:
            RSA.import_key(public_key_str)
            return True
        except:
            return False

    @staticmethod
    def verify_private_key(private_key_str: str) -> bool:
        """
        Verify if a string is a valid RSA private key.
        
        Args:
            private_key_str: Private key in PEM format
            
        Returns:
            True if valid, False otherwise
        """
        try:
            key = RSA.import_key(private_key_str)
            return key.has_private()
        except:
            return False
