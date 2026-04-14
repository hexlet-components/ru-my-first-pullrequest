whats_direction = input("Что мы должны сделать: шифровать или дешифровать? \n").lower()
while whats_direction != "шифровать" and whats_direction != "дешифровать":
    whats_direction = input(
        'Что-то не то ты ввёл. Напиши "шифровать" либо "дешифровать". \n'
    ).lower()


whats_language = input("Какой нужен язык: русский или английский? \n").lower()
while whats_language != "русский" and whats_language != "английский":
    whats_language = input(
        'Что-то не то ты ввёл. Напиши "русский" либо "английский". \n'
    ).lower()


whats_step = input(
    "На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n"
)
while whats_step.isdigit() != True:
    whats_step = input("Что-то не то ты ввёл. Напиши число. \n")


whats_text = input("Какой текст нужно использовать сейчас? \n")
while whats_text.isspace() == True:
    whats_text = input("Что-то не то ты ввёл. Введи текст. \n")


# Объявляем функцию с четырьмя аргументами – соответственно четырем вопросам.
def caesar(direction, language, step, text):

    # Четыре словаря под русские и английские символы, большие и маленькие.
    # В теории можно обойтись без них и обращаться к таблице Unicode.
    # Но мне было удобнее создать свои словари.

    upper_eng_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_rus_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    lower_rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

    # Объявляем цикл for. Количество итераций равно длине строки text.
    for i in range(len(text)):

        # Задаем локальные переменные: длину алфавита и значения словарей.
        if language == "русский":
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        if language == "английский":
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet

        # Если text[i] является буквой:
        if text[i].isalpha():

            # Находим место символа text[i] в словаре upp_alphabet либо low_alphabet.
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            # Если нужно дешифровать, то:
            if direction == "дешифровать":
                # Находим индекс для измененного символа.
                # Новый ндекс = Старый индекс - Шаг % Длина алфавита
                index = (place - int(step)) % alphas

            # Если нужно зашифровать, то:
            elif direction == "шифровать":
                # Находим индекс для измененного символа.
                # Новый ндекс = Старый индекс + Шаг % Длина алфавита
                index = (place + int(step)) % alphas

            # Выводим измененный символ.
            if text[i] == text[i].lower():
                print(low_alphabet[index], end="")
            if text[i] == text[i].upper():
                print(upp_alphabet[index], end="")

        # Если text[i] не является буквой:
        else:
            # Делаем print этого символа бе изменений.
            print(text[i], end="")


caesar(whats_direction, whats_language, whats_step, whats_text)
