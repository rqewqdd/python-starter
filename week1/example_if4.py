# [문제4] 문자열 분석
#
# 다음 문자열을 분석하여 나이가 30미만이고 키가 175이상인 경우에는 YES를 출력하고 아닌 경우에는 NO를 출력하는 프로그램을 작성하시오.
#
# 나이:30,키:180
age = 30
tall = 175

if age < 30 or tall >= 175:
    print('yes')
else:
    print('no')