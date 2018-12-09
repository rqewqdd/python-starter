# [문제3] 홀수 짝수 판별
#
# 주어진 수가 짝수인지 홀수인지 판별하는 프로그램을 작성하시오.

try:
    num = int(input())

    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')

except:
    print('INT형만 입력해주세요.')

# 연습도중 TypeError: not all arguments converted during string formatting 오류가 출력되었는데 num 변수에 입력받은 수가
# str 형태이고 거기에 나머지연산자 %를 써서 오류가 발생했다. 그래서 입력함수인 input을 int 형태로 처리해 결과를 도출했다.
