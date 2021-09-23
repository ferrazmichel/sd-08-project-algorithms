def is_palindrome_iterative(word):
    lowIndex = 0
    highIndex = len(word) - 1
    if word[lowIndex] != word[highIndex]:
        return False
    wordLength = len(word)
    reversedWord = word[wordLength::-1]
    return word == reversedWord
