def is_palindrome_recursive(word, low_index, high_index):

    if word == "":
        return False
    if len(word) <= 1:
        return True
    else:
        return (
            word[low_index] == word[high_index]
            and is_palindrome_recursive(
                word[1: high_index],
                low_index,
                len(word[1: high_index])-1
            )
        )
    