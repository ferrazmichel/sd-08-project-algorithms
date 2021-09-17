def reversed(word, low_index, high_index):
    if len(word) < 2:
        return word
    else:
        return word[high_index] + reversed(word[low_index:high_index], low_index, high_index -1)

def is_palindrome_recursive(word, low_index, high_index):
    return word == reversed(word, low_index, high_index)

# print(is_palindrome_recursive('arara', 0,4))
# print(is_palindrome_recursive('mamao', 0,4))