def is_unique_1(string):
    seen_so_far = {}
    for s in string:
        if (s not in seen_so_far):
            seen_so_far[s] = s
        else:
            return False
    return True