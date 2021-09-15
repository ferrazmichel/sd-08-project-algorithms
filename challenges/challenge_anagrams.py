from collections import Counter


def is_anagram(first_string, second_string):
    """ Faça o código aqui: """
    if (len(first_string) != len(second_string)):
        return False
    elif (Counter(list(first_string)) != Counter(list(second_string))):
        return False
    elif (set(first_string.lower()) == set(second_string.lower())):
        return True
    else:
        return False

# Documentação consultada para a resolução da função acima:
# https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/
# https://stackoverflow.com/questions/4746812/count-the-multiple-occurrences-in-a-set/4746942
# Nenhum dos links traz uma solução 100% correta para esse requisito.
# Contudo, serviu de inspiração para trabalhar
# com Counter e Set ao mesmo tempo
