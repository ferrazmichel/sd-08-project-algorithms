def merge(stringA, stringB):
    left_finger = 0
    right_finger = 0
    result = ""

    while True:
        current_a = stringA[left_finger]
        current_b = stringB[right_finger]

        if current_a <= current_b:
            result += current_a
            left_finger += 1
        else:
            result += current_b
            right_finger += 1

        if left_finger >= len(stringA):
            result += stringB[right_finger:]
            break

        if right_finger >= len(stringB):
            result += stringA[left_finger:]
            break

    return result


def merge_sort(string):
    if len(string) == 1:
        return string

    middle = len(string) // 2
    substringA = string[:middle]
    substringB = string[middle:]

    return merge(merge_sort(substringA), merge_sort(substringB))
