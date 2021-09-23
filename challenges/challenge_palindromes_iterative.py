def is_palindrome_iterative(word):
    wordLength = len(word)
    reversedWord = word[wordLength::-1]
    return word == reversedWord
