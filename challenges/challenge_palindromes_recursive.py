def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    lowercase_word = word.lower()
    word_length = len(lowercase_word)
    if word == "":
        return False
    if word_length < 2:
        return True
    elif lowercase_word[low_index] == lowercase_word[high_index]:
        remaining_words = lowercase_word[1: word_length - 1]
        # print(len(remaining_words) - 1)
        return is_palindrome_recursive(
            remaining_words, 0, len(remaining_words) - 1
        )
    else:
        return False


# word = "ANA"
# is_palindrome_recursive(word, 0, len(word) -1)
