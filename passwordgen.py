import random
print("Password generator")
lowercase = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
uppercase = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
symbol = ('!', '@', '#', '$', '%', '^', '&', '*')
user_length = int(input("Choose the length of your password: "))
while user_length < 8 or user_length > 20:
    user_length = int(input("Wrong input. Length should be between 8 and 20: "))
user_lower = input("Should lowercase symbols be in password? y/n: ")
while user_lower.lower() != 'y' and user_lower.lower() != 'n':
    user_lower = input("Wrong input. Type y for yes and n for no: ")
if user_lower.lower() == 'n':
        user_lower = False
else:
        user_lower = True
user_upper = input("Should uppercase symbols be in password? y/n: ")
while user_upper.lower() != 'y' and user_upper.lower() != 'n':
    user_upper = input("Wrong input. Type y for yes and n for no: ")
if user_upper.lower() == 'n':
        user_upper = False
else:
        user_upper = True
user_symb = input("Should symbols be in password? y/n: ")
while user_symb.lower() != 'y' and user_symb.lower() != 'n':
    user_symb = input("Wrong input. Type y for yes and n for no: ")
if user_symb.lower() == 'n':
        user_symb = False
else:
        user_symb = True
user_num = input("Should numbers be in password? y/n: ")
while user_num.lower() != 'y' and user_num.lower() != 'n':
    user_num = input("Wrong input. Type y for yes and n for no: ")
if user_num.lower() == 'n':
        user_num = False
else:
        user_num = True
available_chars = []
if user_lower == True:
    available_chars.extend(lowercase)
if user_upper == True:
    available_chars.extend(uppercase)
if user_num == True:
    available_chars.extend(num)
if user_symb == True:
    available_chars.extend(symbol)

if len(available_chars) == 0:
    print("Error: You must select at least one character type!")
else:
    password = ''
    for i in range(user_length):
        password += random.choice(available_chars)
    print("Your password is:", password)