# 피보나치 수열 재귀함수로 구현
num = int(input())

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(num))