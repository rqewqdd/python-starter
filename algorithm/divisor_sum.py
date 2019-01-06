def divisor(num):
    sum = 0
    for i in range(1,num+1):
        if num % i == 0:
            sum += i
    return sum

# 결과물
print(divisor(12))

# 다른풀이

def divisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
