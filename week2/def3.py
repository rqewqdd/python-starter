def odd(a):
    if a % 2 == 0:
        return "짝수"
    else:
        return "홀수"

val = int(input())
print(odd(val))