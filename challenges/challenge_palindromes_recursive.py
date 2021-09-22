def is_palindrome_recursive(word, low_index, high_index):
    # print(len(word))
    if not word:
        return False
    else:
        return is_palindrome_recursive(word, low_index, high_index)
