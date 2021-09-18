def is_palindrome_recursive(word, low_index, high_index):

    if word == "":
        return False

    if(low_index == high_index):
        return True

    if word[low_index] == word[high_index]:
        is_palindrome_recursive(word, low_index+1, high_index-1)
    else:
        return False


is_palindrome_recursive('ANA', 0, len('ANA') - 1)
