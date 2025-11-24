import random

lowercase = ('abcdefghijklmnopqrstuvwxyz')
uppercase = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = ('0123456789')
symbol = ('!@#$%^&*')

def get_length(prompt):
    length = int(input(prompt))
    while length < 8 or length > 20:
        print("Wrong input. Choose length in 8-20 range!")
        length = int(input(prompt))
    return length

def get_yes_no_input(type, prompt):
    type = input(prompt)
    while type.lower() not in ['y', 'n', 'yes', 'no']:
        print("Wrong input. Input y for yes and n for no")
        type = input(prompt)
    if type.lower() == 'no' or type.lower() == 'n':
        type = False
    else:
        type = True
    return type

def available_chars():
    chars = ''
    while chars == '':
        use_lowercase = get_yes_no_input('', "Include lowercase letters? (y/n): ")
        use_uppercase = get_yes_no_input('', "Include uppercase letters? (y/n): ")
        use_numbers = get_yes_no_input('', "Include numbers? (y/n): ")
        use_symbols = get_yes_no_input('', "Include symbols? (y/n): ")
        if use_lowercase:
            chars += lowercase
        if use_uppercase:
            chars += uppercase
        if use_numbers:
            chars += num
        if use_symbols:
            chars += symbol
        if chars == '':
            print("You must select at least one character type!")
    return chars

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

def main():
    print("\n" + "="*26)
    print("    PASSWORD GENERATOR")
    print("="*26 + "\n")
    length = get_length("Enter password length (8-20): ")
    chars = available_chars()
    password = generate_password(length, chars)
    print("\n" + "="*44)
    print("Your generated password is:", password)
    print("="*44 + "\n")

if __name__ == "__main__":
    main()