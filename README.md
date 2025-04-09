# Password Generator

A simple Python script that interactively generates a secure random password based on user-selected criteria (uppercase letters, lowercase letters, digits, and special characters). It can also copy the generated password to your clipboard.

# Features

Interactive Prompts: Decide whether to include uppercase letters, lowercase letters, digits, and special characters.
Minimum Length Requirement: Ensures the password is at least 8 characters long.
Clipboard Support: Optionally copy the generated password directly to your system clipboard.

# Dependencies

Python 3.x
pyperclip (for clipboard functionality)

# Getting Started

1) Clone the repository (or download the script):
  git clone https://github.com/yourusername/password-generator.git
  cd password-generator

2) Install dependencies:
   pip install pyperclip

4) Run the script:
   python3 password_generator.py

The script will ask:

Desired password length (must be at least 8)
Whether you want lowercase letters
Whether you want uppercase letters
Whether you want digits
Whether you want special characters
Copy to clipboard (optional): If you choose y when prompted to copy the generated password, it will be stored in your clipboard.

# How It Works

* Prompt the User: The script asks for the desired password length and which character sets to include (lowercase, uppercase, digits, special).
* Generate Candidate Password:
  Uses Python’s secrets module (which provides secure random generation).
  Picks characters randomly from the chosen sets.
* Validate the Password:
  Ensures your choices (e.g., at least one uppercase letter, one lowercase letter, one special character) are actually present.
  Re-generates if conditions are not met.
* Display & (Optionally) Copy:
  Prints out the generated password.
  Optionally, copies it to the clipboard using pyperclip.

# Security Considerations

* Local Machine: The script runs locally, so be mindful of where the generated password is stored or displayed.
* Clipboard: Copying the password places it in your clipboard history. If security is paramount, clear your clipboard (where possible) after use.

# Contributing

Fork the repo on GitHub.
Create a new branch for your feature (git checkout -b feature-name).
Commit your changes (git commit -m "Add awesome feature").
Push to your branch (git push origin feature-name).
Create a pull request on GitHub.
