"""
Main Entry Point
Crypto Toolkit Application

Run this file to start the GUI application:
    python main.py
"""

import tkinter as tk
from gui import CryptoToolkitGUI


def main():
    """
    Main function to start the application.
    """
    root = tk.Tk()
    app = CryptoToolkitGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
