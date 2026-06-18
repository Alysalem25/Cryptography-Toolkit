# SETUP AND EXECUTION GUIDE (Windows)

## 🪟 Windows-Specific Instructions

### Step 1: Verify Python Installation

```powershell
# Open PowerShell and check Python version
python --version

# Output should be: Python 3.7 or higher
# If not found, install from python.org
```

### Step 2: Navigate to Project

```powershell
# Open PowerShell and navigate to project folder
cd d:\crypto_project\crypto_toolkit

# Verify you're in correct location
dir
# Should show: main.py, gui.py, crypto/, utils/, requirements.txt, etc.
```

### Step 3: Install Dependencies

```powershell
# Install required packages
pip install -r requirements.txt

# Or directly:
pip install pycryptodome

# Output should show:
# Successfully installed pycryptodome-3.18.0
```

### Step 4: Verify Installation

```powershell
# Run tests to verify everything works
python example_usage.py

# Should output:
# [OK] All crypto modules imported successfully
# [OK] AES Test: True
# [OK] Base64 Test: True
# ... (more tests)
# [SUCCESS] All basic tests passed!
```

### Step 5: Launch Application

```powershell
# Start the GUI application
python main.py

# GUI window should open immediately
# If it takes a moment, it's loading (normal)
```

---

## 🎯 What You Should See

When you run `python main.py`, a window titled **"Crypto Toolkit"** should open with:

1. **Top area:** Tab buttons:
   - Symmetric Encryption
   - Asymmetric Encryption  
   - Encoding/Decoding
   - Hashing

2. **Main area:** Content for the selected tab

3. **Multiple buttons:** Encrypt, Decrypt, Encode, Decode, Copy, Generate, etc.

---

## 🧪 Testing the Application

### Test 1: AES Encryption

```
1. Click "Symmetric Encryption" tab
2. Algorithm: "AES"
3. Key: "TestKey123"
4. Input: "Hello World"
5. Click [Encrypt]
6. Output: Base64 string appears
7. Click [Decrypt]
8. Output: "Hello World" (matches original)
✓ Test passed if decryption matches original
```

### Test 2: RSA Key Generation

```
1. Click "Asymmetric Encryption" tab
2. Click [Generate RSA Keys (2048-bit)]
3. Wait 2-5 seconds
4. Public and Private keys appear
5. Input: "Secret Message"
6. Click [Encrypt (with Public Key)]
7. Output: Long Base64 string
8. Click [Decrypt (with Private Key)]
9. Output: "Secret Message" (matches original)
✓ Test passed
```

### Test 3: Base64 Encoding

```
1. Click "Encoding/Decoding" tab
2. Type: "Base64"
3. Input: "Test123"
4. Click [Encode]
5. Output: "VGVzdDEyMw=="
6. Click [Decode]
7. Output: "Test123" (matches original)
✓ Test passed
```

### Test 4: SHA-256 Hashing

```
1. Click "Hashing" tab
2. Algorithm: "SHA-256"
3. Input: "password"
4. Click [Generate Hash]
5. Output: 64-character hexadecimal string
6. Output should be consistent (same every time)
✓ Test passed if hash is 64 characters
```

---

## 💡 Helpful Tips

### Copy-Paste Large Content
- For large keys/messages, use Ctrl+C to copy from GUI
- Use Ctrl+V to paste into GUI
- "Copy Output" button copies result automatically

### Keyboard Shortcuts
- Ctrl+A - Select all text
- Ctrl+C - Copy selected text
- Ctrl+V - Paste text
- Tab - Move between fields

### If GUI Doesn't Respond
- Wait a moment (key generation takes time)
- Close window (Ctrl+W or click X)
- Launch again with `python main.py`

### For Longer Operations
- RSA key generation: 2-5 seconds (normal)
- Encryption: < 100ms (fast)
- Large message encryption: might need AES instead of RSA

---

## 📊 Command Reference

```powershell
# Navigate to project
cd d:\crypto_project\crypto_toolkit

# Install dependencies
pip install -r requirements.txt

# Run all tests
python example_usage.py

# Start GUI application
python main.py

# View test data samples
python TEST_DATA.py

# Check Python version
python --version

# List installed packages
pip list
```

---

## 🔍 Project File Locations

| File | Purpose | Size |
|------|---------|------|
| main.py | Entry point | ~20 lines |
| gui.py | GUI interface | ~600 lines |
| crypto/symmetric.py | AES/DES/3DES | ~300 lines |
| crypto/asymmetric.py | RSA | ~150 lines |
| crypto/encoding.py | Base64/Hex/URL | ~100 lines |
| crypto/hashing.py | MD5/SHA | ~80 lines |
| utils/helpers.py | Utilities | ~80 lines |
| example_usage.py | Testing | ~200 lines |
| TEST_DATA.py | Test reference | ~300 lines |
| requirements.txt | Dependencies | 1 line |
| README.md | Full docs | ~400 lines |

---

## 🚨 Troubleshooting on Windows

### Problem 1: Python not found
```powershell
# Solution: Reinstall Python from python.org
# Make sure to check "Add Python to PATH" during installation
```

### Problem 2: "permission denied" when installing
```powershell
# Solution: Run PowerShell as Administrator
# Right-click PowerShell → Run as administrator
# Then run: pip install pycryptodome
```

### Problem 3: GUI window appears but freezes
```powershell
# This is usually normal during RSA key generation
# Wait 3-5 seconds for it to complete
```

### Problem 4: "module 'tkinter' not found"
```powershell
# Solution: Install tkinter
# Python 3.8+: Usually included
# If missing: pip install tk
```

### Problem 5: Cannot paste text into GUI
```powershell
# Try: Click in text field, then Ctrl+V
# Or: Right-click and select paste (if available)
```

---

## ✅ Verification Steps

After setup, verify everything works:

```powershell
# Step 1: Navigate to project
cd d:\crypto_project\crypto_toolkit

# Step 2: Check files exist
ls
# Should list: main.py, gui.py, crypto folder, etc.

# Step 3: Verify dependencies
pip show pycryptodome
# Should show version 3.18.0 or higher

# Step 4: Run tests
python example_usage.py
# Should complete with [SUCCESS] message

# Step 5: Launch application
python main.py
# GUI should open
```

---

## 📈 Performance Tips

### For Best Performance:
- Close other applications
- Use AES for large files (faster than RSA)
- RSA is best for small messages only
- Hashing is instant (always fast)

### Approximate Speeds:
- AES encryption: < 10ms for typical message
- DES encryption: < 5ms
- 3DES encryption: < 10ms
- RSA key generation: 2-5 seconds
- Base64 encoding: instant
- SHA-256 hashing: instant

---

## 🎓 University Submission

### Files to Include:
1. All Python files (main.py, gui.py, crypto/*, utils/*)
2. requirements.txt
3. README.md
4. PROJECT_SUMMARY.md
5. Screenshots of GUI in action

### How to Take Screenshots:
1. Run `python main.py`
2. Use Windows Snipping Tool (Win+Shift+S)
3. Capture each tab with example content
4. Save as PNG/JPG

### Demo Sequence for Presentation:
```
1. Show file structure
2. Run: python example_usage.py
3. Run: python main.py
4. Demo AES encryption
5. Demo RSA key generation
6. Demo Base64 encoding
7. Demo SHA-256 hashing
8. Discuss code quality and security
```

---

## 📞 Quick Reference

### Most Common Commands:

```powershell
# Setup (do once)
cd d:\crypto_project\crypto_toolkit
pip install -r requirements.txt

# Testing (do before first use)
python example_usage.py

# Daily use (run application)
python main.py

# Debugging (view test data)
python TEST_DATA.py
```

### Exit Application:
- Click X button on window
- Or press Alt+F4
- Or use Ctrl+C in terminal

---

## ✨ You're All Set!

The application is ready to use. Just run:

```powershell
python main.py
```

And the GUI will open immediately.

Enjoy your Crypto Toolkit! 🔐
