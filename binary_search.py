def binary_search(element, some_list):

    left_index = 0
    right_index = (len(some_list) - 1)

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = some_list[middle_index]

        if element == middle_value:
            return middle_index

        elif element < middle_value:

            right_index = middle_index - 1

        elif element > middle_value:
            left_index = middle_index + 1

    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))