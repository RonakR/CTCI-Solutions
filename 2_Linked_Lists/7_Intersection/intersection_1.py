def intersection_1(firstll, secondll):
    diff = len(firstll) - len(secondll)

    if diff > 0:
        firstll = fix_length(firstll, diff)
    elif diff < 0:
        secondll = fix_length(secondll, abs(diff))

    return find_intersection(firstll, secondll)

def fix_length(ll, diff):
    while diff:
        ll = ll.next
        diff -= 1
    return ll

def find_intersection(firstll, secondll):
    intersection = False

    currentfll = firstll
    currentsll = secondll

    while currentfll is not None:
        if not intersection:
            if currentfll.data is not currentsll.data or currentfll.next is not currentsll.next:
                intersection = False
        if not intersection and (currentfll.data == currentsll.data and currentfll.next == currentsll.next):
            intersection = currentfll

        currentfll = currentfll.next
        currentsll = currentsll.next

    return intersection