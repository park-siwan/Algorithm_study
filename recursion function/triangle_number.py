# 1부터 n까지의 합을리턴
def triangle_number(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return triangle_number(n - 1) + n

for i in range(1, 11):
    print(triangle_number(i))