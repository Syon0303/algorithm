n, m = map(int, input().split())

# direction : 0 = 북쪽,  1 = 동쪽, 2 = 남쪽, 3 = 서쪽
# 시작 좌표 및 바라보는 방향 입력
x, y, direction = map(int, input().split())

# 방문한 위치 생성
visit_location = [[0] * m for _ in range(n)]
visit_location[x][y] = 1

# 맵 생성
my_map = []
for i in range(n):
    my_map.append(list(map(int, input().split())))

# 차레대로 북쪽, 동쪽, 남쪽, 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 가본 곳 수를 세는 변수
count = 1
turn_count = 0

while True:
    direction -= 1
    if direction == -1:
        direction = 3

    #print(x)
    
    # 가려고 하는 곳
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 갈 수 있을 때
    if visit_location[nx][ny] == 0 and my_map[nx][ny] == 0:
        visit_location[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
    
    # 갈 수 없을 때(바다이거나, 가본 곳이거나)
    else:
        turn_count += 1
    
    # 네 방향 아무곳도 갈 수 없는 경우
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있는 경우 (바다만 아니면 됨)
        if my_map[x][y] == 0:
            x = nx
            y = ny
            turn_count = 0
        
        # 뒤가 바다인 경우
        else:
            break

print(count)