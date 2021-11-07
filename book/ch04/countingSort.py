# =계수 정렬
#0부터 9까지 임의의 배열 생성 (모든 원소의 값이 0보다 크거나 같다고 가정)
array = [8, 7, 9, 3, 4, 5, 2, 1, 6, 0, 8, 7, 9, 3, 4, 5, 2, 1, 6, 0]

# max(array) = 9 이므로, len(count) = 10
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
