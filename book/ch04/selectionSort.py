# 선택 정렬
#0부터 9까지 임의의 배열 생성
array = [8, 7, 9, 3, 4, 5, 2, 1, 6, 0]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)