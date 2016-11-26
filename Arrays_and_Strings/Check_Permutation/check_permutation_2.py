def check_permutation_2(first_string, second_string):
    if not len(first_string) == len(second_string): return False

    hash_table = {}
    for char in first_string:
        if (char not in hash_table):
            hash_table[char] = 1
        else:
            hash_table[char] = hash_table[char]+1

    for s in second_string:
        if s in hash_table and hash_table[s] is not 0:
            hash_table[s] = hash_table[s] - 1
        else:
            return False
    return True