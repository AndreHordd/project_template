from app.io.input import *
from app.io.output import *


def main():
    console_text = read_text_from_console()
    file_text = read_text_from_file("data/text.txt")
    data = read_data_with_pandas("data/text.txt")

    print_to_console("Console text: " + console_text)
    print_to_console("File text: " + file_text)
    print_to_console("Data from file :")
    print_to_console(str(data))

    combined_text = (
            "Console text: " + console_text + "\n" +
            "File text: " + file_text + "\n" +
            "Data from file :\n" + str(data)
    )
    write_text_to_file(combined_text, "data/output.txt")

if __name__ == "__main__":
    main()