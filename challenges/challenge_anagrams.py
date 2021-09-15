def is_anagram(first_string, second_string):
    if len(first_string) == len(second_string):
        if (freq(first_string) == freq(second_string)):
            return True
        return False
    else:
        return False


# https://www.quora.com/How-can-I-compare-two-words-on-Python-3-and-check-if-they-are-anagrams-of-each-other-specifically-without-the-use-of-built-in-functions
def freq(word):
    freq_dict = {}
    for char in word:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict
