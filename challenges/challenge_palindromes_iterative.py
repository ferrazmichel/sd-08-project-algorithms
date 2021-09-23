def is_palindrome_iterative(word):
    if not word:
        return False
    wordLength = len(word)
    reversedWord = word[wordLength::-1]
    return word == reversedWord
