def urlify_1(string, length):
    string = string.strip()
    stringList = string.split(" ")
    return '%20'.join(stringList)
