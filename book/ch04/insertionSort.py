# 삽입 정렬
#0부터 9까지 임의의 배열 생성
array = [8, 7, 9, 3, 4, 5, 2, 1, 6, 0]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]

print(array)

'''
# 책의 풀이
array = [8, 7, 9, 3, 4, 5, 2, 1, 6, 0]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

# 의문점 : 굳이 else 문이 들어갈 이유를 모르겠음
'''