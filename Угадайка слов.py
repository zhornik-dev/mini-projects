import random

words_with_hints = {
    "PYTHON": "Язык программирования, названный в честь комедийного шоу", 
    "DEVELOPER": "Человек, который пишет код", 
    "PROGRAMMING": "Процесс создания компьютерных программ", 
    "ALGORITHM": "Последовательность шагов для решения задачи", 
    "FUNCTION": "Блок кода, который можно вызывать по имени", 
    "VARIABLE": "Контейнер для хранения данных", 
    "STRING": "Тип данных для текста", 
    "LIST": "Изменяемая последовательность элементов",  
    "DICTIONARY": "Коллекция пар ключ-значение", 
    "LOOP": "Конструкция для повторения действий"
    }

def get_word():
    word = random.choice(list(words_with_hints.keys()))
    hint = words_with_hints[word]
    return word, hint

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word, hint):
    print("Подсказка:", hint)

    word_completion = '_' * len(word)                                         # строка, содержащая символы «_» на каждую букву задуманного слова
    word_completion = word[0] + word_completion[1:-1] + word[-1]              # открываем первую и последнюю букву
    guessed = False                                                           # сигнальная метка
    guessed_letters = []                                                      # список уже названных букв
    guessed_words = []                                                        # список уже названных слов
    tries = 6                                                                 # количество попыток

    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)

    while (
        not guessed and
        tries > 0
    ):
        user_input = input("Введите букву или слово: ").upper()
        if len(user_input) == 1:
            if user_input not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("Можно вводить только английские буквы.")
                continue
            if user_input in guessed_letters:
                print("Вы уже называли эту букву.")
                continue
            guessed_letters.append(user_input)
            if user_input in word:
                print("Хороший ход!")
                for i in range(len(word)):
                    if word[i] == user_input:
                        word_completion = word_completion[:i] + user_input + word_completion[i+1:]
                print(display_hangman(tries))
                print(word_completion)
                if "_" not in word_completion:
                    guessed = True
            else:
                print("Такой буквы нет в слове.")
                tries -= 1
                print(display_hangman(tries))
        else:
            if user_input in guessed_words:
                print("Вы уже называли это слово.")
                continue
            guessed_words.append(user_input)
            if user_input == word:
                guessed = True
                word_completion = word
                break
            else:
                print("Неверно!")
                tries -= 1
                print(display_hangman(tries))

    if guessed:
        print("Поздравляем, вы угадали слово! Вы победили!")
    else:
        print(display_hangman(0))
        print(f"Вы проиграли. Загаданное слово: {word}")

while True:
    word, hint = get_word()
    play(word, hint)
    again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
    if again != "да":
        print("Спасибо за игру! До встречи.")
        break