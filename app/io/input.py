def input_from_console():
    """
    Отримує текстовий ввід від користувача з консолі.

    Повертає:
        str: Введений користувачем текст.
    """
    return input("Введіть текст: ")

def read_from_file_full(filename):
    """
    Зчитує весь вміст текстового файлу як один рядок.

    Аргументи:
        filename (str): Шлях до файлу.

    Повертає:
        str: Вміст файлу.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def read_from_file_lines(filename):
    """
    Зчитує текстовий файл пострічково у вигляді списку та об'єднує в один рядок.

    Аргументи:
        filename (str): Шлях до файлу.

    Повертає:
        str: Об'єднані рядки з файлу.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return ''.join(lines)
