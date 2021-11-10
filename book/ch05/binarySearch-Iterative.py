# 반복문을 사용한 이진 탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("값이 배열 내에 존재하지 않습니다.")
else:
    print("찾는 원소의 위치는 " + str(result + 1) + "번째에 있습니다.")