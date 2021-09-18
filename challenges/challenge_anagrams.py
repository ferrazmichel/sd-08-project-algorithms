# algoritmo utilizado -> shell sort
def my_sort(string):
    h = len(string) // 2
    while h > 0:
        i = h
        while i < len(string):
            temp = string[i]
            changed = False
            j = i - h
            while j >= 0 and string[j] > temp:
                string[j + h] = string[j]
                changed = True
                j -= h
                if changed:
                    string[j + h] = temp
                i += 1
        h = h // 2


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return my_sort(list(first_string)) == my_sort(list(second_string))


if __name__ == "__main__":

    first_string = "amor"
    second_string = "roma"
    print(is_anagram(first_string, second_string))

    first_string = "pedra"
    second_string = "perda"
    print(is_anagram(first_string, second_string))

    first_string = "pato"
    second_string = "tapo"
    print(is_anagram(first_string, second_string))

    first_string = "coxinha"
    second_string = "empada"
    print(is_anagram(first_string, second_string))

    first_string = "pedra"
    second_string = "pedro"
    print(is_anagram(first_string, second_string))
