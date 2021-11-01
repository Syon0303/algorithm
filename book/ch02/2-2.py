# 나의 풀이
t = 0
count = 0
n = int(input()) + 1

# 0 ~ 59사이의 3이 포함되는 수의 개수(t) 구하기
# find() 함수로 찾지 못한다면 -1을 반환하기에 != -1 사용
for i in range(60):
    if str(i).find('3') != -1:
        t += 1

# 0 < n < 24 이므로 n의 10의자리는 없으므로 n의 1의자리만 계산
# int -> float(또는 double)로의 묵시적 형변환을 막았음
for i in range(n):
    if i - ((int(i/10))*10) == 3:
        count += 1
    
result = ((t*60) + ((60-t)*t)) * (n-count) + count*60*60

print(result)

'''
책의 풀이
h = int(input())

count = 0
for i in range(h + 1):
    for j in rnage(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1
print(count)
'''