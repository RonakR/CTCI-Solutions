def urlify_2(string, length):
    stringList = list(string)
    lastIndex = len(string)-1
    for i in range(length-1, -1, -1):
        if stringList[i] is not " ":
            stringList[lastIndex] = stringList[i]
            lastIndex-=1
        else:
            stringList[lastIndex] = '0'
            stringList[lastIndex-1] = '2'
            stringList[lastIndex-2] = '%'
            lastIndex-=3
    return ''.join(stringList)
