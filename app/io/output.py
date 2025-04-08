def output_to_console(text):
    """
    Виводить текст у консоль.

    Аргументи:
        text (str): Текст, який потрібно вивести.
    """
    print(text)

def write_to_file_builtin(filename, text):
    """
    Записує текст у файл за допомогою вбудованих засобів Python.

    Аргументи:
        filename (str): Ім'я файлу.
        text (str): Текст, який потрібно записати.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
