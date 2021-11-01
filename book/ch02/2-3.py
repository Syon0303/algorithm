#왕실의 나이트
#나의 풀이
coordinate = input()
my_coordinate = (int(coordinate[1]), ord(coordinate[0]) - 96)

count = 0

numOfCase = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

for num in numOfCase:
    next_row = my_coordinate[0] + num[0]
    next_column = my_coordinate[1] + num[1]

    if next_row <= 8 and next_row >= 1 and next_column <=8 and next_column >= 1:
        count += 1

print(count)

#책의 답은 나의 풀이와 유사하므로 적지 않음.