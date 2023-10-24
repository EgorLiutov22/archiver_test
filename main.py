def archiver(text_string: str) -> str:
    """
    text_string: str
    :return: str
    """
    char_count = 0
    result = []
    for i in range(len(text_string) - 1):
        if text_string[i] == text_string[i + 1]:
            char_count += 1
        else:
            result.append(add_char(text_string[i], char_count + 1))
            char_count = 0
        if i == len(text_string) - 2:
            result.append(add_char(text_string[i], char_count + 1))
    result = ''.join(result)
    return result


def add_char(char: str, char_count: int) -> str:
    """
    char: str
    char_count: int
    :return : str
    """
    if char_count == 1:
        return char
    else:
        return char + str(char_count)


def unpacker(text_string: str) -> str:
    """
        text_string: str
        :return: str
        """
    result = []
    for i in range(len(text_string)):
        if not text_string[i].isdigit():
            if text_string[i + 1].isdigit():
                result.append(text_string[i] * int(text_string[i + 1]))
            else:
                result.append(text_string[i])
    result = ''.join(result)
    return result


if __name__ == '__main__':
    text = 'aaabbccccc'
    archived = archiver(text)
    print(archived)
    unpacked = unpacker(archived)
    print(unpacked)
