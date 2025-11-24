# Password Generator

A simple command-line password generator written in Python that creates random passwords based on user preferences.

## Features

- Generate passwords with customizable length (8-20 characters)
- Choose which character types to include:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Symbols (!@#$%^&*)
- Input validation to ensure secure password requirements
- User-friendly console interface

## Requirements

- Python 3.x

## How to Use

1. Run the program:
   ```bash
   python passwordgen.py
   ```

2. Follow the prompts:
   - Enter desired password length (between 8 and 20 characters)
   - Choose which character types to include (y/n for each option)
   - Your generated password will be displayed

## Example

```
==========================
    PASSWORD GENERATOR
==========================

Enter password length (8-20): 12
Include lowercase letters? (y/n): y
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n

============================================
Your generated password is: aB3kLmNpQrXy
============================================
```

## Functions

- `get_length(prompt)` - Validates and returns password length
- `get_yes_no_input(type, prompt)` - Gets yes/no user input
- `available_chars()` - Builds character set based on user choices
- `generate_password(length, chars)` - Generates random password
- `main()` - Main program loop

## Notes

- At least one character type must be selected
- Invalid inputs will prompt the user to try again

## License

MIT License
