def is_anagram(first_string, second_string):
    firstStringList = list(first_string)
    firstStringList.sort()
    secondStringList = list(second_string)
    secondStringList.sort()
    return (firstStringList == secondStringList)
