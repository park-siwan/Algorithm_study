def min_coin_count(value, coin_list):

    coin_list.sort(reverse=True)
    total = []
    for i in range(len(coin_list)):
        coin_range = (value // coin_list[i])
        total.append(coin_range)
        exchange = value % coin_list[i]
        if exchange == 0:
            return sum(total)
        else:
            value -= (coin_range * coin_list[i])
    return sum(total)

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list)) # 10
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))