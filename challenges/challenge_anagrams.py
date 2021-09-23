def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    firstStringList = list(first_string)
    secondStringList = list(second_string)
    firstStringList.sort()
    secondStringList.sort()
    return (firstStringList == secondStringList)
