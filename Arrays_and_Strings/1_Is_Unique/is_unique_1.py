def is_unique_1(string):
    if (string == "" or type(string) is not str): return "Please input a string with characters."
    if (len(string) > 128): return False
    seen_so_far = {}
    for s in string:
        if (s not in seen_so_far):
            seen_so_far[s] = s
        else:
            return False
    return True