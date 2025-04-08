from input import input_from_console, read_from_file_full, read_from_file_lines
from output import output_to_console, write_to_file_builtin

def main():
    console_text = input_from_console()
    output_to_console(console_text)
    write_to_file_builtin("output_console.txt", console_text)

    file_text_full = read_from_file_full("example.txt") 
    output_to_console(file_text_full)
    write_to_file_builtin("output_file_full.txt", file_text_full)

    file_text_lines = read_from_file_lines("example.txt")
    output_to_console(file_text_lines)
    write_to_file_builtin("output_file_lines.txt", file_text_lines)

if __name__ == "__main__":
    main()
