"""
Symmetric Encryption Module
Handles AES, DES, and 3DES encryption/decryption operations.
"""

import os
import base64
from Crypto.Cipher import AES, DES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class SymmetricEncryption:
    """
    Handles symmetric encryption operations.
    Supports AES, DES, and 3DES algorithms.
    """

    # Block size for AES and DES
    AES_BLOCK_SIZE = 16
    DES_BLOCK_SIZE = 8

    @staticmethod
    def _validate_key(key: str, algorithm: str) -> bytes:
        """
        Validate and format the key for the specified algorithm.
        
        Args:
            key: Secret key as string
            algorithm: Name of algorithm (AES, DES, 3DES)
            
        Returns:
            Properly formatted key as bytes
            
        Raises:
            ValueError: If key size is invalid for the algorithm
        """
        key_bytes = key.encode('utf-8')
        
        if algorithm == 'AES':
            # AES supports 16, 24, or 32 bytes (128, 192, 256 bits)
            if len(key_bytes) not in [16, 24, 32]:
                # Pad or truncate to nearest valid size
                if len(key_bytes) < 16:
                    key_bytes = key_bytes.ljust(16, b'\0')
                elif len(key_bytes) < 24:
                    key_bytes = key_bytes[:24]
                elif len(key_bytes) < 32:
                    key_bytes = key_bytes[:32]
                else:
                    key_bytes = key_bytes[:32]
        
        elif algorithm == 'DES':
            # DES requires exactly 8 bytes (64 bits)
            if len(key_bytes) < 8:
                key_bytes = key_bytes.ljust(8, b'\0')
            else:
                key_bytes = key_bytes[:8]
        
        elif algorithm == '3DES':
            # 3DES requires 16 or 24 bytes (2 or 3 keys of 8 bytes each)
            if len(key_bytes) < 16:
                key_bytes = key_bytes.ljust(16, b'\0')
            else:
                key_bytes = key_bytes[:24]
        
        return key_bytes

    @staticmethod
    def encrypt_aes(plaintext: str, key: str) -> str:
        """
        Encrypt plaintext using AES encryption.
        
        Args:
            plaintext: Text to encrypt
            key: Secret key
            
        Returns:
            Base64-encoded ciphertext with IV prepended
        """
        try:
            key_bytes = SymmetricEncryption._validate_key(key, 'AES')
            plaintext_bytes = plaintext.encode('utf-8')
            
            # Generate random IV
            iv = get_random_bytes(SymmetricEncryption.AES_BLOCK_SIZE)
            
            # Create cipher and encrypt
            cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(plaintext_bytes, SymmetricEncryption.AES_BLOCK_SIZE))
            
            # Combine IV + ciphertext and encode to base64
            combined = iv + ciphertext
            return base64.b64encode(combined).decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"AES Encryption Error: {str(e)}")

    @staticmethod
    def decrypt_aes(ciphertext: str, key: str) -> str:
        """
        Decrypt AES-encrypted ciphertext.
        
        Args:
            ciphertext: Base64-encoded ciphertext with IV
            key: Secret key
            
        Returns:
            Decrypted plaintext
        """
        try:
            key_bytes = SymmetricEncryption._validate_key(key, 'AES')
            combined = base64.b64decode(ciphertext)
            
            # Extract IV and ciphertext
            iv = combined[:SymmetricEncryption.AES_BLOCK_SIZE]
            ciphertext_bytes = combined[SymmetricEncryption.AES_BLOCK_SIZE:]
            
            # Decrypt
            cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext_bytes), SymmetricEncryption.AES_BLOCK_SIZE)
            
            return plaintext.decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"AES Decryption Error: {str(e)}")

    @staticmethod
    def encrypt_des(plaintext: str, key: str) -> str:
        """
        Encrypt plaintext using DES encryption.
        
        Args:
            plaintext: Text to encrypt
            key: Secret key (8 characters minimum)
            
        Returns:
            Base64-encoded ciphertext with IV prepended
        """
        try:
            key_bytes = SymmetricEncryption._validate_key(key, 'DES')
            plaintext_bytes = plaintext.encode('utf-8')
            
            # Generate random IV
            iv = get_random_bytes(SymmetricEncryption.DES_BLOCK_SIZE)
            
            # Create cipher and encrypt
            cipher = DES.new(key_bytes, DES.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(plaintext_bytes, SymmetricEncryption.DES_BLOCK_SIZE))
            
            # Combine IV + ciphertext and encode to base64
            combined = iv + ciphertext
            return base64.b64encode(combined).decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"DES Encryption Error: {str(e)}")

    @staticmethod
    def decrypt_des(ciphertext: str, key: str) -> str:
        """
        Decrypt DES-encrypted ciphertext.
        
        Args:
            ciphertext: Base64-encoded ciphertext with IV
            key: Secret key
            
        Returns:
            Decrypted plaintext
        """
        try:
            key_bytes = SymmetricEncryption._validate_key(key, 'DES')
            combined = base64.b64decode(ciphertext)
            
            # Extract IV and ciphertext
            iv = combined[:SymmetricEncryption.DES_BLOCK_SIZE]
            ciphertext_bytes = combined[SymmetricEncryption.DES_BLOCK_SIZE:]
            
            # Decrypt
            cipher = DES.new(key_bytes, DES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext_bytes), SymmetricEncryption.DES_BLOCK_SIZE)
            
            return plaintext.decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"DES Decryption Error: {str(e)}")

    @staticmethod
    def encrypt_3des(plaintext: str, key: str) -> str:
        """
        Encrypt plaintext using 3DES encryption.
        
        Args:
            plaintext: Text to encrypt
            key: Secret key (16 or 24 characters minimum)
            
        Returns:
            Base64-encoded ciphertext with IV prepended
        """
        try:
            key_bytes = SymmetricEncryption._validate_key(key, '3DES')
            plaintext_bytes = plaintext.encode('utf-8')
            
            # Generate random IV
            iv = get_random_bytes(SymmetricEncryption.DES_BLOCK_SIZE)
            
            # Create cipher and encrypt
            cipher = DES3.new(key_bytes, DES3.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(plaintext_bytes, SymmetricEncryption.DES_BLOCK_SIZE))
            
            # Combine IV + ciphertext and encode to base64
            combined = iv + ciphertext
            return base64.b64encode(combined).decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"3DES Encryption Error: {str(e)}")

    @staticmethod
    def decrypt_3des(ciphertext: str, key: str) -> str:
        """
        Decrypt 3DES-encrypted ciphertext.
        
        Args:
            ciphertext: Base64-encoded ciphertext with IV
            key: Secret key
            
        Returns:
            Decrypted plaintext
        """
        try:
            key_bytes = SymmetricEncryption._validate_key(key, '3DES')
            combined = base64.b64decode(ciphertext)
            
            # Extract IV and ciphertext
            iv = combined[:SymmetricEncryption.DES_BLOCK_SIZE]
            ciphertext_bytes = combined[SymmetricEncryption.DES_BLOCK_SIZE:]
            
            # Decrypt
            cipher = DES3.new(key_bytes, DES3.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext_bytes), SymmetricEncryption.DES_BLOCK_SIZE)
            
            return plaintext.decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"3DES Decryption Error: {str(e)}")
