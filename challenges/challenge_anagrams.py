def is_anagram(first_string, second_string):
    if not first_string:
        return False
    if not second_string:
        return False
    firstStringList = list(first_string)
    firstStringList.sort()
    secondStringList = list(second_string)
    secondStringList.sort()
    return (firstStringList == secondStringList)
