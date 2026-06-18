"""
Hashing Module
Handles MD5 and SHA-256 hashing operations.
"""

import hashlib


class Hashing:
    """
    Handles cryptographic hashing operations.
    Supports MD5, SHA-256, and other algorithms.
    """

    @staticmethod
    def hash_md5(text: str) -> str:
        """
        Generate MD5 hash of text.
        
        Args:
            text: Text to hash
            
        Returns:
            Hexadecimal MD5 hash
        """
        try:
            text_bytes = text.encode('utf-8')
            md5_hash = hashlib.md5(text_bytes)
            return md5_hash.hexdigest()
        except Exception as e:
            raise ValueError(f"MD5 Hashing Error: {str(e)}")

    @staticmethod
    def hash_sha256(text: str) -> str:
        """
        Generate SHA-256 hash of text.
        
        Args:
            text: Text to hash
            
        Returns:
            Hexadecimal SHA-256 hash
        """
        try:
            text_bytes = text.encode('utf-8')
            sha256_hash = hashlib.sha256(text_bytes)
            return sha256_hash.hexdigest()
        except Exception as e:
            raise ValueError(f"SHA-256 Hashing Error: {str(e)}")

    @staticmethod
    def hash_sha1(text: str) -> str:
        """
        Generate SHA-1 hash of text.
        
        Args:
            text: Text to hash
            
        Returns:
            Hexadecimal SHA-1 hash
        """
        try:
            text_bytes = text.encode('utf-8')
            sha1_hash = hashlib.sha1(text_bytes)
            return sha1_hash.hexdigest()
        except Exception as e:
            raise ValueError(f"SHA-1 Hashing Error: {str(e)}")

    @staticmethod
    def hash_sha512(text: str) -> str:
        """
        Generate SHA-512 hash of text.
        
        Args:
            text: Text to hash
            
        Returns:
            Hexadecimal SHA-512 hash
        """
        try:
            text_bytes = text.encode('utf-8')
            sha512_hash = hashlib.sha512(text_bytes)
            return sha512_hash.hexdigest()
        except Exception as e:
            raise ValueError(f"SHA-512 Hashing Error: {str(e)}")
