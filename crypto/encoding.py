"""
Encoding Module
Handles Base64, Hex, and URL encoding/decoding operations.
"""

import base64
import urllib.parse


class Encoding:
    """
    Handles various encoding and decoding operations.
    Supports Base64, Hexadecimal, and URL encoding.
    """

    @staticmethod
    def encode_base64(text: str) -> str:
        """
        Encode text to Base64.
        
        Args:
            text: Text to encode
            
        Returns:
            Base64-encoded string
        """
        try:
            text_bytes = text.encode('utf-8')
            base64_bytes = base64.b64encode(text_bytes)
            return base64_bytes.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Base64 Encoding Error: {str(e)}")

    @staticmethod
    def decode_base64(encoded_text: str) -> str:
        """
        Decode Base64-encoded text.
        
        Args:
            encoded_text: Base64-encoded string
            
        Returns:
            Decoded text
        """
        try:
            base64_bytes = encoded_text.encode('utf-8')
            text_bytes = base64.b64decode(base64_bytes)
            return text_bytes.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Base64 Decoding Error: {str(e)}")

    @staticmethod
    def encode_hex(text: str) -> str:
        """
        Encode text to Hexadecimal.
        
        Args:
            text: Text to encode
            
        Returns:
            Hexadecimal-encoded string
        """
        try:
            text_bytes = text.encode('utf-8')
            return text_bytes.hex()
        except Exception as e:
            raise ValueError(f"Hex Encoding Error: {str(e)}")

    @staticmethod
    def decode_hex(hex_text: str) -> str:
        """
        Decode Hexadecimal-encoded text.
        
        Args:
            hex_text: Hexadecimal-encoded string
            
        Returns:
            Decoded text
        """
        try:
            # Remove spaces if any
            hex_text = hex_text.replace(' ', '')
            text_bytes = bytes.fromhex(hex_text)
            return text_bytes.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Hex Decoding Error: {str(e)}")

    @staticmethod
    def encode_url(text: str) -> str:
        """
        Encode text using URL encoding.
        
        Args:
            text: Text to encode
            
        Returns:
            URL-encoded string
        """
        try:
            return urllib.parse.quote(text)
        except Exception as e:
            raise ValueError(f"URL Encoding Error: {str(e)}")

    @staticmethod
    def decode_url(encoded_text: str) -> str:
        """
        Decode URL-encoded text.
        
        Args:
            encoded_text: URL-encoded string
            
        Returns:
            Decoded text
        """
        try:
            return urllib.parse.unquote(encoded_text)
        except Exception as e:
            raise ValueError(f"URL Decoding Error: {str(e)}")
