def solution(price, money, count):
    price_count = 0
    for price_index in range(count):
        price_count = price_count + price * (price_index + 1)
    if money > price_count:
        return 0
    else: return price_count - money