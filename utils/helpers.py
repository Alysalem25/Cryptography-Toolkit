"""
Helper Functions Module
General utility functions for the Crypto Toolkit.
"""

import re


def format_key_display(key: str, max_length: int = 50) -> str:
    """
    Format a key for display in GUI (truncate if necessary).
    
    Args:
        key: Key string to format
        max_length: Maximum length to display
        
    Returns:
        Formatted key string
    """
    if len(key) > max_length:
        return key[:max_length] + "..."
    return key


def validate_key_format(key: str, key_type: str = 'general') -> tuple:
    """
    Validate key format based on type.
    
    Args:
        key: Key to validate
        key_type: Type of key ('general', 'rsa_public', 'rsa_private')
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not key or len(key.strip()) == 0:
        return False, "Key cannot be empty"
    
    if key_type == 'rsa_public':
        if '-----BEGIN PUBLIC KEY-----' not in key:
            return False, "Invalid RSA public key format"
        if '-----END PUBLIC KEY-----' not in key:
            return False, "Invalid RSA public key format"
    
    elif key_type == 'rsa_private':
        if '-----BEGIN RSA PRIVATE KEY-----' not in key and '-----BEGIN PRIVATE KEY-----' not in key:
            return False, "Invalid RSA private key format"
        if '-----END RSA PRIVATE KEY-----' not in key and '-----END PRIVATE KEY-----' not in key:
            return False, "Invalid RSA private key format"
    
    return True, ""


def copy_to_clipboard(text: str) -> bool:
    """
    Copy text to clipboard (platform-independent approach using Tkinter).
    
    Args:
        text: Text to copy
        
    Returns:
        True if successful, False otherwise
    """
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        root.destroy()
        return True
    except:
        return False


def split_text_into_chunks(text: str, chunk_size: int = 100) -> list:
    """
    Split text into chunks for display purposes.
    
    Args:
        text: Text to split
        chunk_size: Size of each chunk
        
    Returns:
        List of text chunks
    """
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
