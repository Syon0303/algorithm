# 퀵 정렬
#0부터 9까지 임의의 배열 생성
array = [5, 7, 9, 3, 4, 8, 2, 1, 6, 0]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))