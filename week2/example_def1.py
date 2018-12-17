# [문제1] 홀수 짝수 판별

# # 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성하시오.

def is_odd(val):
    if val % 2 == 0:
        print('짝수')
    else:
        print('홀수')

num = int(input())
is_odd(num)
