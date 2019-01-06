# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

def solution(str):
    answer = int(str)
    return answer

# 결과물
str = "1234"
print(solution(str))

# 다른풀이

def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result

