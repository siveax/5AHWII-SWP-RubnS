def create_char_number_dict(start_char, end_char):
    """
    Creates a dictionary with characters from start_char to end_char as keys and numbers starting at 0 as values.

    Return: dict
    """

    result_dict = {}
    curr_index = 0

    # ord('a') = 97, ord('z') = 122 (ASCII)
    start_code = ord(start_char)
    end_code = ord(end_char)

    for code in range(start_code, end_code + 1):
        char = chr(code)

        result_dict[char] = curr_index

        curr_index += 1

    return result_dict


def main():
    """
    Main function to execute the program.
    It creates a dictionary for a fixed character range
    and prints the resulting dictionary.
    """

    alphabet_dict = create_char_number_dict('a', 'z')
    print(alphabet_dict)


if __name__ == '__main__':
    main()