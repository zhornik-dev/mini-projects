direction = input("Выберите направление (шифрование/дешифрование/взломать): ")
language_of_the_alphabet = input("Выберите язык (русский/английский): ")
text = input("Введите текст: ")

if direction == "взломать":
    if language_of_the_alphabet == "русский":
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

    for shift_step in range(len(alphabet)):
        result = ""
        for c in text:
            if c.isalpha():
                is_upper = c.isupper()
                c = c.lower()
                index = alphabet.find(c)
                if index == -1:  # символ не найден в алфавите
                    result += c
                    continue
                new_index = (index - shift_step) % len(alphabet)  # расшифровка = сдвиг влево
                new_c = alphabet[new_index]
                if is_upper:
                    new_c = new_c.upper()
                result += new_c
            else:
                result += c
        print(f"Сдвиг {shift_step:2d}: {result}")
else:
    shift_step = int(input("Введите шаг сдвига: "))
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
            if index == -1:
                result += c
                continue
            new_index = (index + shift_step) % len(alphabet)
            new_c = alphabet[new_index]
            if is_upper:
                new_c = new_c.upper()
            result += new_c
        else:
            result += c
    print(result)