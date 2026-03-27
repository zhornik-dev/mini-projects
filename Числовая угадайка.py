import random

print("Добро пожаловать в числовую угадайку")

def is_valid(string_argument, right_border):
    return (
        string_argument.isdigit() and
        1 <= int(string_argument) <= right_border
    )

while True:

    while True:
        enter_right_border = input("Введите правую границу чисел (от 1 до n): ")

        if (
            enter_right_border.isdigit() and
            int(enter_right_border) >= 2
            ):
            right_border = int(enter_right_border)
            break
        
        print("Нужно ввести целое число, большее или равное 2")

    random_number = random.randint(1, right_border)
    counter = 0

    while True:
        user_input = input(f"Введите число от 1 до {right_border}: ")
        
        if not is_valid(user_input, right_border):
            print(f"А может быть, всё-таки введём целое число от 1 до {right_border}?")
            continue
        
        user_number = int(user_input)
        counter += 1
        
        if user_number < random_number:
            print("Ваше число меньше загаданного, попробуйте ещё разок")
        elif user_number > random_number:
            print("Ваше число больше загаданного, попробуйте ещё разок")
        else:
            print(f"Вы угадали за {counter} попыток, поздравляем!")
            break

    user_response = input("Хотите сыграть ещё? (да/нет): ").lower()

    if user_response != "да":
        print("Спасибо, что играли в числовую угадайку. Ещё увидимся...")
        break