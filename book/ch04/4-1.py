# 위에서 아래로
# 나의 풀이
data = list(map(int, input().split()))
data.sort()

for i in range(len(data)):
    print(data[len(data)-i-1])

'''
# 책의 풀이
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array = sorted(array, reverse = True)
for i in array:
    print(i, end = ' ')

# sorted 함수의 reverse 인자를 몰랐음.
'''