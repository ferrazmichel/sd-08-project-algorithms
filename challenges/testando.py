# def reverse(list):
#     reversed_list = []
#     for item in list:
#         reversed_list.insert(0, item)
#     return reversed_list


# def reverse(list):
#     if len(list) < 2:
#         return list
#     else:
#         print(list[0])
#         return reverse(list[1:]) + [list[0]]

# print(reverse([1, 2, 3, 4, 5]))


# array = [1, 2, 3, 4, 5]

# print(array[2:])
tups = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

for a, b in tups:
    for i in range(a, b + 1):
        print(i)

# print(range(5, 7))