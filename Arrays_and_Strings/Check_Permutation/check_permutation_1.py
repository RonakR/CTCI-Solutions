def check_permutation_1(first_string, second_string):
    if not len(first_string) == len(second_string): return False

    second_list = list(second_string)
    for s in first_string:
        if s in second_list:
            second_list.pop(second_list.index(s))
        else:
            return False
    return True