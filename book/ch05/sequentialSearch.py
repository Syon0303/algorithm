# 순차 탐색
# 나의 풀이
print("생성할 원소 개수를 입력한 후, 한 칸 띄고 찾을 문자열을 입력하시오")
temp = input().split()
n = int(temp[0])
my_string = temp[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하시오. (단, 구분은 띄어쓰기 한 칸으로 구분함)")
array = input().split()


for i in range(n):
    if array[i] == my_string:
        print("찾을 문자열의 위치는 " + str(i+1) + "번째에 있습니다.")
        break
    
    if i == n-1:
        print("문자열이 없습니다.")

'''
#책의 풀이
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print("생성할 원소 개수를 입력한 후, 한 칸 띄고 찾을 문자열을 입력하시오")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하시오. (단, 구분은 띄어쓰기 한 칸으로 구분함)")
array = input().split()

print(sequential_search(n, targert, array))
'''