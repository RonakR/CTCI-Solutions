def intersection_1(firstll, secondll):
    diff = len(firstll) - len(secondll)
    headfll, headsll = firstll.head, secondll.head

    if diff > 0:
        headfll = fix_length(headfll, diff)
    elif diff < 0:
        headfll = fix_length(headsll, abs(diff))

    return find_intersection(headfll, headsll)

def fix_length(ll, diff):
    while diff:
        ll = ll.next
        diff -= 1
    return ll

def find_intersection(headfll, headsll):
    intersection = False

    currentfll = headfll
    currentsll = headsll

    while currentfll is not None:
        if not intersection:
            if currentfll is not currentsll:
                intersection = False
        if not intersection and (currentfll == currentsll):
            intersection = currentfll

        currentfll = currentfll.next
        currentsll = currentsll.next

    return intersection