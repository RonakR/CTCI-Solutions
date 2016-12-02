def palindrome_permutation_1(string):
    charFrequency = []
    string = string.lower()
    for char in string:
        if char is not " ":
            if(char in charFrequency):
                charFrequency.remove(char)
            else:
                charFrequency.append(char)

    return not(len(charFrequency) >= 2)