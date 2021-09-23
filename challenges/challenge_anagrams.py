def merge(stringA, stringB):
    leftFinger = 0
    rightFinger = 0
    result = ""

    while True:
        currentStringA = stringA[leftFinger]
        currentStringB = stringB[rightFinger]
        if currentStringA <= currentStringB:
            result += currentStringA
            leftFinger += 1
        else:
            result += currentStringB
            rightFinger += 1
        if leftFinger >= len(stringA):
            result += stringB[rightFinger:]
            break
        if rightFinger >= len(stringB):
            result += stringA[leftFinger:]
            break
    return result


def mergeSort(string):
    if len(string) == 1:
        return string

    middle = len(string) // 2
    stringA = string[:middle]
    stringB = string[middle:]
    return merge(mergeSort(stringA), mergeSort(stringB))


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return mergeSort(first_string) == mergeSort(second_string)
