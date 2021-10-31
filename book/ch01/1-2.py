#나의 풀이
n, m, k = map(int, input().split())
data_n = list(map(int, input().split()))

data_n.sort()

first = data_n[n-1]
second = data_n[n-2]

result = (first * k + second) * (m // (k+1))
result += first * (m % (k+1))

print(result)

'''
책의 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
'''