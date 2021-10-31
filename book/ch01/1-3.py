#나의 풀이
n, m = map(int, input().split())
temp = 0
max_data = 0

for i in range(n):
    row = list(map(int, input().split()))
    temp = min(row)
    if temp >= max_data:
        max_data = temp

print(max_data)

'''
책의 풀이
- min() 함수를 이용하는 방법
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

-2중 for 문을 사용하는 방법
n, m = map(int ,input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)
'''