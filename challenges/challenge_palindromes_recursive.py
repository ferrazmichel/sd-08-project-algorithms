def is_palindrome_recursive(word, low_index, high_index):
    """Função recursiva para verificar se uma palavra é palindrome."""
    if word == '':
        return False
      
    if (high_index - low_index) <= 2:
      if word[low_index] == word[high_index]:
        return True
      else:
        return False

    else:
      return is_palindrome_recursive(word, low_index + 1, high_index - 1)
