def find_duplicate(numbers):
    sortedNumbers = sorted(numbers)
    for numberA, numberB in zip(sortedNumbers, sortedNumbers[1:]):
        if numberA == numberB and min(numberA, numberB) > 0:
            return numberA
    return False
