# 정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.

def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 결과물
num = 2
print(solution(num))

# 다른풀이

def evenOrOdd(num):
    return num % 2 and "Odd" or "Even"

# 삼항연산자 : 연산자(operator)의 피연산자(operand) 개수가 3개라서 "삼항 연산자
# 조건 and 참인경우 or 거짓인경우