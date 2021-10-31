# 나의 풀이
MAX_RANGE = 100000
MIN_RANGE = 2

n, k = map(int, input().split())
count = 0

if n > MAX_RANGE or n < MIN_RANGE or k < MIN_RANGE or k > MAX_RANGE:
    print("out of range")

elif n >= k:
    while True:
        if n % k == 0:
            n /= k
        else:
            n -= 1
    
        count += 1
        if n == 1:
            break
        
    print(count)

elif n <= k:
    print("n is less than k")

'''
책의 풀이
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
'''