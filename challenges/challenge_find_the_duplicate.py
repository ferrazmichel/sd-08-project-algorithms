def search(array, value):
    """busca por um valor dentro de um array"""
    for element in array:
        if element == value:
            return value


def find_duplicate(nums):
    """Encontra número duplicados em um array."""
    if not nums:
        return False

    ordenado = sorted(nums)
    for idx, num in enumerate(ordenado):
        if not isinstance(num, int) or num < 0:
            return False
        repetido = search(ordenado[idx + 1:], num)
        if repetido:
            return repetido

    return False
