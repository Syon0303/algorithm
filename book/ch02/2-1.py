#나의 풀이
n = map(int, input().split())
plans = list(input().split())
plan_list = ['L', 'R', 'U', 'D']
location = [1, 1]

for plan in plans:
    if plan == 'L':
        if location[1] == 1:
            continue
        location[1] += -1

    elif plan == 'R':
        if location[1] == n:
            continue
        location[1] += 1

    elif plan == 'U':
        if location[0] == 1:
            continue
        location[0] -= 1

    elif plan == 'D':
        if location[0] == n:
            continue
        location[0] += 1

print(location)

'''
#책의 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
'''