def is_unique_2(string):
    if (string == "" or type(string) is not str): return "Please input a string with characters."
    if (len(string) > 128): return False
    string = sorted(string.lower())
    l = len(string)
    for i in range(0, l-1, 1):
        if(string[i] == string[i+1]):
            return False
    return True