def is_palindrome_iterative(word):
    high_index = len(word) - 1
    low_index = 0
    if not word:
        return False
    for i in range(len(word)//2):
        if word[high_index] != word[low_index]:
            return False
        low_index += 1
        high_index -= 1
    return True
