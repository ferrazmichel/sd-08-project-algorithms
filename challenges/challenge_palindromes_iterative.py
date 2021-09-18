def is_palindrome_iterative(word):
    if word == '':
        return False

    reverseWord = word[::-1]

    if reverseWord == word:
        return True
    else:
        return False

    """ if word == '':
        return False
    last_index = len(word)-1
    start_index = 0
    while start_index != last_index:
        if start_index == last_index:
            break
        if word[start_index] == word[last_index]:
            last_index = last_index - 1
            start_index = start_index + 1
        else:
            return False """
