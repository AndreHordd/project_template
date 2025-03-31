def print_to_console(text: str):
    """
    Prints text to the console.

    Examples:
        >>> print_to_console("Test")
        (Console output: Test)

    Args:
        text (str): The text to print.

    Returns:
        None
    """
    print("Executing print_to_console")
    print(text)


def write_text_to_file(text: str, filename: str):
    """
    Writes text to a file using built-in Python functionality.

    Examples:
        >>> write_text_to_file("Test", "data/text.txt")
        (File data/text.txt will contain: Test)

    Args:
        text (str): The text to write.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    print("Executing write_text_to_file")
    with open(filename, "w") as file:
        file.write(text)
