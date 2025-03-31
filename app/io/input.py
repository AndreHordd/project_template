def read_text_from_console():
    """
    Reads text from the console.

    Examples:
        Input: Test
        >>> read_text_from_console()
        Enter text: //Test

    Returns:
        str: The text entered by user.
    """
    print("Executing read_text_from_console")
    return input("Enter text: ")


def read_text_from_file(filename: str):
    """
    Reads text from a file using built-in Python functionality.

    Examples:
        If data/text.txt contains:
            Test
        >>> read_text_from_file("data/text.txt")
        "Test"

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The text read from the file.
    """
    print("Executing read_text_from_file")
    with open(filename, "r") as file:
        return file.read()


def read_data_with_pandas(filename: str):
    """
    Reads data from a text file using pandas.
    The file is read line by line and each line becomes a row in a DataFrame.

    Examples:
        If data/text.txt contains:
            Line 1
            Line 2
        >>> read_data_with_pandas("data/text.txt")
              text
        0  Line 1
        1  Line 2

    Args:
        filename (str): The name of the text file to read from.

    Returns:
        DataFrame: A DataFrame with one column "text" containing each line of the file.
    """
    print("Executing read_data_with_pandas")
    import pandas as pd
    with open(filename, "r") as file:
        lines = file.readlines()

    lines = [line.rstrip("\n") for line in lines]
    df = pd.DataFrame(lines, columns=["text"])
    return df
