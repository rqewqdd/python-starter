# [문제2] 평균값 계산
#
# 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. (단, 입력으로 들어오는 수의 갯수는 정해져 있지 않다.)

def average(*avg):
    result = 0
    for i in avg:
        result += i
    result = result / len(avg)
    print(result)
average(1,2,3)

# *변수명 = 튜플 변수, **변수명 = 딕셔너리 변수
