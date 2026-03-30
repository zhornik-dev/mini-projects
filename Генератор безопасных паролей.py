import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""
number_of_passwords = int(input("Сколько паролей генерировать? "))
length_of_one_password = int(input("Длина одного пароля: "))

if input("Включать цифры? (да/нет): ").lower() == "да":
    chars += digits

if input("Включать заглавные буквы? (да/нет): ").lower() == "да":
    chars += uppercase_letters

if input("Включать строчные буквы? (да/нет): ").lower() == "да":
    chars += lowercase_letters

if input("Включать спецсимволы? (да/нет): ").lower() == "да":
    chars += punctuation

if input("Исключать неоднозначные символы (il1Lo0O)? (да/нет): ").lower() == "да":

    for c in "il1Lo0O":
        chars = chars.replace(c, "")

def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

for _ in range(number_of_passwords):
    print(generate_password(length_of_one_password, chars))