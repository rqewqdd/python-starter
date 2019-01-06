# String형 배열 seoul의 element중 Kim의 위치 x를 찾아,
# 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.
# seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

def solution(seoul):
    answer = seoul.index("Kim")
    return "김서방은 %d에 있다" %answer

# 결과물
seoul = ["Jane","Kim"]
print(solution(seoul))

# index() : list에 위치값

# 다른풀이
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# {} .format()을 이용해서 문자라던지 숫자를 지정해줄수 있는거같다.