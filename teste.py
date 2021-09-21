def selection_sort(string):
    array = list(string)
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]

    return ''.join(array)


print(selection_sort("pato"))