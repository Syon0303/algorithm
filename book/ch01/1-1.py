# 나의 풀이
n = int(input())
coin_type = [500, 100, 50, 10]
count = 0

for coin in coin_type:
    while True:
        if n//coin == 0:
            break
        else:
            n -= coin
            count += 1
print(count)

'''
정답
n = int(input())
count = 0

#큰 단위 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += coin
    n %= coin

print(count)
'''