# def find_duplicate(nums):
#     counter = 0
#     size = len(nums)
#     if size <= 2:
#         return False
#     tested_position = 0
#     while tested_position < size:
#         # tested_number = nums[tested_position]
#         # for number in nums[tested_position + 1]:
#         #     if number > 0 or counter == 2:
#         #         return False
#         #     if tested_number == number:
#         #         counter += 1
#         tested_position += 1
#     if counter == 1:
#         return True

# def devide(list):
#     size = len(list)
#     if size > 2:

#     elif size == 2:
#         if list[0] == list[1]:


def find_duplicate(nums):
    counter_equals = 0
    recursive(nums, counter_equals)
    print(counter_equals)
    if counter_equals == 1:
        return True
    return False


def recursive(nums, counter_equals):
    size = len(nums)
    if size > 2:
        bigger = []
        smaller = []
        tested_number = nums[0]
        for number in nums[1:]:
            if number > tested_number:
                bigger.append(number)
            elif number < tested_number:
                smaller.append(number)
            else:
                counter_equals += 1
        recursive(smaller, counter_equals)
        recursive(bigger, counter_equals)
    elif size == 2 and nums[0] == nums[1]:
        counter_equals += 1
