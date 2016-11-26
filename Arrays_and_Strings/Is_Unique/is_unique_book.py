def is_unique_book(string):
    if (string == "" or type(string) is not str): return "Please input a string with characters."
    if (len(string) > 128): return False

    char_set = [False for _ in range(128)]
    for s in string:
        val = ord(s)
        if(char_set[val]):
            return False

        char_set[val] = True
    return True