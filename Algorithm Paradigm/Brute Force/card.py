def max_product(left_number, right_number):
    max_product = -1

    for left in left_number:
        for right in right_number:
            max_product = max(max_product, left * right)

    return max_product


print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))