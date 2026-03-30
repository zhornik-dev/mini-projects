direction = input("Выберите направление (шифрование/дешифрование): ")
language_of_the_alphabet = input("Выберите язык (русский/английский): ")
shift_step = int(input("Введите шаг сдвига: "))
text = input("Введите текст: ")

if direction == "дешифрование":
    shift_step = -shift_step

if language_of_the_alphabet == "русский":
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
else:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

result = ""

for c in text:
    if c.isalpha():
        is_upper = c.isupper()
        c = c.lower()
        index = alphabet.find(c)
        new_index = (index + shift_step) % len(alphabet)
        if is_upper:
            new_c = alphabet[new_index].upper()
        else:
            new_c = alphabet[new_index]
        result += new_c
    else:
        result += c

print(result)