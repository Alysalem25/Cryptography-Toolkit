"""
GUI Module
Tkinter-based graphical user interface for the Crypto Toolkit.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import threading

from crypto import SymmetricEncryption, AsymmetricEncryption, Encoding, Hashing
from utils.helpers import format_key_display, copy_to_clipboard


class CryptoToolkitGUI:
    """
    Main GUI class for the Crypto Toolkit application.
    """

    def __init__(self, root):
        """
        Initialize the GUI application.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Crypto Toolkit")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)

        # Configure style
        style = ttk.Style()
        style.theme_use('clam')

        # Create main layout
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface."""
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Create tabs
        self.tab_symmetric = ttk.Frame(self.notebook)
        self.tab_asymmetric = ttk.Frame(self.notebook)
        self.tab_encoding = ttk.Frame(self.notebook)
        self.tab_hashing = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_symmetric, text="Symmetric Encryption")
        self.notebook.add(self.tab_asymmetric, text="Asymmetric Encryption")
        self.notebook.add(self.tab_encoding, text="Encoding/Decoding")
        self.notebook.add(self.tab_hashing, text="Hashing")

        # Setup each tab
        self.setup_symmetric_tab()
        self.setup_asymmetric_tab()
        self.setup_encoding_tab()
        self.setup_hashing_tab()

    def setup_symmetric_tab(self):
        """Set up the symmetric encryption tab."""
        main_frame = ttk.Frame(self.tab_symmetric, padding="10")
        main_frame.pack(fill='both', expand=True)

        # Algorithm selection
        alg_frame = ttk.LabelFrame(main_frame, text="Algorithm", padding="10")
        alg_frame.pack(fill='x', pady=5)

        ttk.Label(alg_frame, text="Select Algorithm:").pack(side='left', padx=5)
        self.sym_algorithm = ttk.Combobox(alg_frame, values=['AES', 'DES', '3DES'], state='readonly', width=15)
        self.sym_algorithm.set('AES')
        self.sym_algorithm.pack(side='left', padx=5)

        # Key input
        key_frame = ttk.LabelFrame(main_frame, text="Secret Key", padding="10")
        key_frame.pack(fill='x', pady=5)

        ttk.Label(key_frame, text="Enter Key:").pack(side='left', padx=5)
        self.sym_key = ttk.Entry(key_frame, width=50, show='*')
        self.sym_key.pack(side='left', padx=5, fill='x', expand=True)

        # Input text
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="10")
        input_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(input_frame, text="Plaintext/Ciphertext:").pack(anchor='w', padx=5, pady=2)
        self.sym_input = scrolledtext.ScrolledText(input_frame, height=8, width=80)
        self.sym_input.pack(fill='both', expand=True, padx=5, pady=5)

        # Output text
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding="10")
        output_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(output_frame, text="Result:").pack(anchor='w', padx=5, pady=2)
        self.sym_output = scrolledtext.ScrolledText(output_frame, height=8, width=80, state='disabled')
        self.sym_output.pack(fill='both', expand=True, padx=5, pady=5)

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=10)

        ttk.Button(btn_frame, text="Encrypt", command=self.encrypt_symmetric).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Decrypt", command=self.decrypt_symmetric).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Copy Output", command=lambda: self.copy_output(self.sym_output)).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=lambda: self.clear_fields(self.sym_input, self.sym_output)).pack(side='left', padx=5)

    def setup_asymmetric_tab(self):
        """Set up the asymmetric encryption tab."""
        main_frame = ttk.Frame(self.tab_asymmetric, padding="10")
        main_frame.pack(fill='both', expand=True)

        # Key generation section
        keygen_frame = ttk.LabelFrame(main_frame, text="RSA Key Generation", padding="10")
        keygen_frame.pack(fill='x', pady=5)

        ttk.Button(keygen_frame, text="Generate RSA Keys (2048-bit)", command=self.generate_rsa_keys).pack(side='left', padx=5)

        # Public key
        pubkey_frame = ttk.LabelFrame(main_frame, text="Public Key", padding="10")
        pubkey_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(pubkey_frame, text="Public Key (for encryption):").pack(anchor='w', padx=5, pady=2)
        self.asym_public_key = scrolledtext.ScrolledText(pubkey_frame, height=6, width=80)
        self.asym_public_key.pack(fill='both', expand=True, padx=5, pady=5)

        pubkey_btn_frame = ttk.Frame(pubkey_frame)
        pubkey_btn_frame.pack(fill='x', padx=5)
        ttk.Button(pubkey_btn_frame, text="Copy", command=lambda: self.copy_output(self.asym_public_key)).pack(side='left', padx=2)

        # Private key
        privkey_frame = ttk.LabelFrame(main_frame, text="Private Key", padding="10")
        privkey_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(privkey_frame, text="Private Key (for decryption):").pack(anchor='w', padx=5, pady=2)
        self.asym_private_key = scrolledtext.ScrolledText(privkey_frame, height=6, width=80)
        self.asym_private_key.pack(fill='both', expand=True, padx=5, pady=5)

        privkey_btn_frame = ttk.Frame(privkey_frame)
        privkey_btn_frame.pack(fill='x', padx=5)
        ttk.Button(privkey_btn_frame, text="Copy", command=lambda: self.copy_output(self.asym_private_key)).pack(side='left', padx=2)

        # Input/Output for encryption/decryption
        io_frame = ttk.LabelFrame(main_frame, text="Encryption/Decryption", padding="10")
        io_frame.pack(fill='both', expand=True, pady=5)

        # Input
        ttk.Label(io_frame, text="Input Text:").pack(anchor='w', padx=5, pady=2)
        self.asym_input = scrolledtext.ScrolledText(io_frame, height=4, width=80)
        self.asym_input.pack(fill='both', expand=True, padx=5, pady=5)

        # Buttons
        btn_frame = ttk.Frame(io_frame)
        btn_frame.pack(fill='x', padx=5, pady=5)

        ttk.Button(btn_frame, text="Encrypt (with Public Key)", command=self.encrypt_asymmetric).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Decrypt (with Private Key)", command=self.decrypt_asymmetric).pack(side='left', padx=5)

        # Output
        ttk.Label(io_frame, text="Result:").pack(anchor='w', padx=5, pady=2)
        self.asym_output = scrolledtext.ScrolledText(io_frame, height=4, width=80, state='disabled')
        self.asym_output.pack(fill='both', expand=True, padx=5, pady=5)

        result_btn_frame = ttk.Frame(io_frame)
        result_btn_frame.pack(fill='x', padx=5)
        ttk.Button(result_btn_frame, text="Copy Output", command=lambda: self.copy_output(self.asym_output)).pack(side='left', padx=2)
        ttk.Button(result_btn_frame, text="Clear", command=lambda: self.clear_fields(self.asym_input, self.asym_output)).pack(side='left', padx=2)

    def setup_encoding_tab(self):
        """Set up the encoding/decoding tab."""
        main_frame = ttk.Frame(self.tab_encoding, padding="10")
        main_frame.pack(fill='both', expand=True)

        # Encoding type selection
        enc_frame = ttk.LabelFrame(main_frame, text="Encoding Type", padding="10")
        enc_frame.pack(fill='x', pady=5)

        ttk.Label(enc_frame, text="Select Encoding:").pack(side='left', padx=5)
        self.enc_type = ttk.Combobox(enc_frame, values=['Base64', 'Hexadecimal', 'URL'], state='readonly', width=15)
        self.enc_type.set('Base64')
        self.enc_type.pack(side='left', padx=5)

        # Input text
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="10")
        input_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(input_frame, text="Text:").pack(anchor='w', padx=5, pady=2)
        self.enc_input = scrolledtext.ScrolledText(input_frame, height=8, width=80)
        self.enc_input.pack(fill='both', expand=True, padx=5, pady=5)

        # Output text
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding="10")
        output_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(output_frame, text="Result:").pack(anchor='w', padx=5, pady=2)
        self.enc_output = scrolledtext.ScrolledText(output_frame, height=8, width=80, state='disabled')
        self.enc_output.pack(fill='both', expand=True, padx=5, pady=5)

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=10)

        ttk.Button(btn_frame, text="Encode", command=self.encode).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Decode", command=self.decode).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Copy Output", command=lambda: self.copy_output(self.enc_output)).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=lambda: self.clear_fields(self.enc_input, self.enc_output)).pack(side='left', padx=5)

    def setup_hashing_tab(self):
        """Set up the hashing tab."""
        main_frame = ttk.Frame(self.tab_hashing, padding="10")
        main_frame.pack(fill='both', expand=True)

        # Algorithm selection
        alg_frame = ttk.LabelFrame(main_frame, text="Hash Algorithm", padding="10")
        alg_frame.pack(fill='x', pady=5)

        ttk.Label(alg_frame, text="Select Algorithm:").pack(side='left', padx=5)
        self.hash_algorithm = ttk.Combobox(alg_frame, values=['MD5', 'SHA-1', 'SHA-256', 'SHA-512'], state='readonly', width=15)
        self.hash_algorithm.set('SHA-256')
        self.hash_algorithm.pack(side='left', padx=5)

        # Input text
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="10")
        input_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(input_frame, text="Text to Hash:").pack(anchor='w', padx=5, pady=2)
        self.hash_input = scrolledtext.ScrolledText(input_frame, height=8, width=80)
        self.hash_input.pack(fill='both', expand=True, padx=5, pady=5)

        # Output text
        output_frame = ttk.LabelFrame(main_frame, text="Hash Output", padding="10")
        output_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(output_frame, text="Hash Result:").pack(anchor='w', padx=5, pady=2)
        self.hash_output = scrolledtext.ScrolledText(output_frame, height=8, width=80, state='disabled')
        self.hash_output.pack(fill='both', expand=True, padx=5, pady=5)

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=10)

        ttk.Button(btn_frame, text="Generate Hash", command=self.generate_hash).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Copy Output", command=lambda: self.copy_output(self.hash_output)).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=lambda: self.clear_fields(self.hash_input, self.hash_output)).pack(side='left', padx=5)

    # Symmetric encryption operations
    def encrypt_symmetric(self):
        """Perform symmetric encryption."""
        try:
            plaintext = self.sym_input.get("1.0", tk.END).strip()
            key = self.sym_key.get().strip()
            algorithm = self.sym_algorithm.get()

            if not plaintext or not key:
                messagebox.showerror("Error", "Please enter text and key")
                return

            if algorithm == 'AES':
                ciphertext = SymmetricEncryption.encrypt_aes(plaintext, key)
            elif algorithm == 'DES':
                ciphertext = SymmetricEncryption.encrypt_des(plaintext, key)
            elif algorithm == '3DES':
                ciphertext = SymmetricEncryption.encrypt_3des(plaintext, key)

            self.set_output(self.sym_output, ciphertext)
            messagebox.showinfo("Success", "Encryption successful!")

        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed:\n{str(e)}")

    def decrypt_symmetric(self):
        """Perform symmetric decryption."""
        try:
            ciphertext = self.sym_input.get("1.0", tk.END).strip()
            key = self.sym_key.get().strip()
            algorithm = self.sym_algorithm.get()

            if not ciphertext or not key:
                messagebox.showerror("Error", "Please enter ciphertext and key")
                return

            if algorithm == 'AES':
                plaintext = SymmetricEncryption.decrypt_aes(ciphertext, key)
            elif algorithm == 'DES':
                plaintext = SymmetricEncryption.decrypt_des(ciphertext, key)
            elif algorithm == '3DES':
                plaintext = SymmetricEncryption.decrypt_3des(ciphertext, key)

            self.set_output(self.sym_output, plaintext)
            messagebox.showinfo("Success", "Decryption successful!")

        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed:\n{str(e)}")

    # Asymmetric encryption operations
    def generate_rsa_keys(self):
        """Generate RSA key pair."""
        try:
            # Run in separate thread to avoid GUI freezing
            thread = threading.Thread(target=self._generate_keys_thread)
            thread.start()
        except Exception as e:
            messagebox.showerror("Error", f"Key generation failed:\n{str(e)}")

    def _generate_keys_thread(self):
        """Generate keys in background thread."""
        try:
            messagebox.showinfo("Generating", "Generating RSA keys... This may take a moment.")
            public_key, private_key = AsymmetricEncryption.generate_rsa_keys(2048)

            self.set_output(self.asym_public_key, public_key)
            self.set_output(self.asym_private_key, private_key)

            self.root.after(0, lambda: messagebox.showinfo("Success", "RSA keys generated successfully!"))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Key generation failed:\n{str(e)}"))

    def encrypt_asymmetric(self):
        """Perform asymmetric encryption."""
        try:
            plaintext = self.asym_input.get("1.0", tk.END).strip()
            public_key = self.asym_public_key.get("1.0", tk.END).strip()

            if not plaintext:
                messagebox.showerror("Error", "Please enter text to encrypt")
                return

            if not public_key:
                messagebox.showerror("Error", "Please provide a public key")
                return

            if len(plaintext) > 190:
                messagebox.showerror("Error", "Text too long for RSA encryption (max ~190 characters)")
                return

            ciphertext = AsymmetricEncryption.encrypt_rsa(plaintext, public_key)
            self.set_output(self.asym_output, ciphertext)
            messagebox.showinfo("Success", "Encryption successful!")

        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed:\n{str(e)}")

    def decrypt_asymmetric(self):
        """Perform asymmetric decryption."""
        try:
            ciphertext = self.asym_input.get("1.0", tk.END).strip()
            private_key = self.asym_private_key.get("1.0", tk.END).strip()

            if not ciphertext:
                messagebox.showerror("Error", "Please enter ciphertext to decrypt")
                return

            if not private_key:
                messagebox.showerror("Error", "Please provide a private key")
                return

            plaintext = AsymmetricEncryption.decrypt_rsa(ciphertext, private_key)
            self.set_output(self.asym_output, plaintext)
            messagebox.showinfo("Success", "Decryption successful!")

        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed:\n{str(e)}")

    # Encoding operations
    def encode(self):
        """Perform encoding operation."""
        try:
            text = self.enc_input.get("1.0", tk.END).strip()
            enc_type = self.enc_type.get()

            if not text:
                messagebox.showerror("Error", "Please enter text to encode")
                return

            if enc_type == 'Base64':
                result = Encoding.encode_base64(text)
            elif enc_type == 'Hexadecimal':
                result = Encoding.encode_hex(text)
            elif enc_type == 'URL':
                result = Encoding.encode_url(text)

            self.set_output(self.enc_output, result)
            messagebox.showinfo("Success", "Encoding successful!")

        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed:\n{str(e)}")

    def decode(self):
        """Perform decoding operation."""
        try:
            text = self.enc_input.get("1.0", tk.END).strip()
            enc_type = self.enc_type.get()

            if not text:
                messagebox.showerror("Error", "Please enter text to decode")
                return

            if enc_type == 'Base64':
                result = Encoding.decode_base64(text)
            elif enc_type == 'Hexadecimal':
                result = Encoding.decode_hex(text)
            elif enc_type == 'URL':
                result = Encoding.decode_url(text)

            self.set_output(self.enc_output, result)
            messagebox.showinfo("Success", "Decoding successful!")

        except Exception as e:
            messagebox.showerror("Error", f"Decoding failed:\n{str(e)}")

    # Hashing operations
    def generate_hash(self):
        """Generate hash."""
        try:
            text = self.hash_input.get("1.0", tk.END).strip()
            algorithm = self.hash_algorithm.get()

            if not text:
                messagebox.showerror("Error", "Please enter text to hash")
                return

            if algorithm == 'MD5':
                hash_result = Hashing.hash_md5(text)
            elif algorithm == 'SHA-1':
                hash_result = Hashing.hash_sha1(text)
            elif algorithm == 'SHA-256':
                hash_result = Hashing.hash_sha256(text)
            elif algorithm == 'SHA-512':
                hash_result = Hashing.hash_sha512(text)

            self.set_output(self.hash_output, hash_result)
            messagebox.showinfo("Success", "Hash generated successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Hashing failed:\n{str(e)}")

    # Utility methods
    def set_output(self, text_widget, content):
        """Set output text widget content."""
        text_widget.config(state='normal')
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", content)
        text_widget.config(state='disabled')

    def copy_output(self, text_widget):
        """Copy output to clipboard."""
        try:
            content = text_widget.get("1.0", tk.END).strip()
            if content:
                if copy_to_clipboard(content):
                    messagebox.showinfo("Success", "Copied to clipboard!")
                else:
                    messagebox.showwarning("Warning", "Could not copy to clipboard")
            else:
                messagebox.showwarning("Warning", "Nothing to copy")
        except Exception as e:
            messagebox.showerror("Error", f"Copy failed:\n{str(e)}")

    def clear_fields(self, input_widget, output_widget):
        """Clear input and output fields."""
        input_widget.delete("1.0", tk.END)
        self.set_output(output_widget, "")
