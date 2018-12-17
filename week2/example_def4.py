# [문제4] 피보나치
#
# 입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.
#
# 피보나치 수열은 다음과 같은 순서로 결과값을 리턴한다.
#
# fib(0) → 0 리턴
# fib(1) → 1 리턴
# fib(2) → fib(0) + fib(1) → 0 + 1 → 1 리턴
# fib(3) → fib(1) + fib(2) → 1 + 1 → 2 리턴
# fib(4) → fib(2) + fib(3) → 1 + 2 → 3 리턴
#
# 피보나치 수는 첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열이다 >> 1 1 2 3 5 8 13

def fibo(val):
    if val == 0:
        return val
    elif val == 1:
        return val
    elif val > 1:
        return (val-1) + (val-2)

num = int(input())
for i in range(num):
    print(fibo(i))