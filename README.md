# Password Generator

A command-line password generator built with Python. Create secure, customizable passwords with multiple character type options and length control.

## Features

- 🔢 Custom password length (8-20 characters)
- 🔤 Choose character types to include:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&*)
- ✔️ Input validation for all user choices
- 🎲 Randomized generation for security
- 🚫 Prevents weak passwords (minimum 8 characters)

## Requirements

- Python 3.x

## Setup

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
```

2. Run the program:
```bash
   python password_generator.py
```

## How to Use

1. Choose your password length (8-20)
2. Select which character types to include (y/n):
   - Lowercase letters
   - Uppercase letters
   - Symbols
   - Numbers
3. Your secure password will be generated instantly!

## Example Usage
```
Password generator
Choose the length of your password: 12
Should lowercase symbols be in password? y/n: y
Should uppercase symbols be in password? y/n: y
Should symbols be in password? y/n: y
Should numbers be in password? y/n: n
Your password is: aB@mKpL#xWqT
```

## How It Works

- Uses Python's `random` module for secure randomization
- Validates all user inputs to prevent errors
- Builds a character pool based on your selections
- Randomly selects characters from the pool to create your password

## Security Note

This generator creates strong passwords when using multiple character types and longer lengths. For maximum security:
- Use all character types
- Choose length 12+ characters
- Avoid using the same password across multiple sites

## Future Improvements

- [ ] Generate multiple password options at once
- [ ] Add password strength indicator
- [ ] Copy to clipboard functionality
- [ ] Exclude ambiguous characters option (0/O, 1/l/I)
- [ ] Save passwords securely to encrypted file

## License

MIT License
