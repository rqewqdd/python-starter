# 딕셔너리 최소값
#
# 다음과 같은 딕셔너리 a가 있다.
#
# >>> a = {'A':90, 'B':80, 'C':70}
# 딕셔너리 a의 value중에서 최소 값을 출력하시오.
#
# (힌트. 여러개의 요소값중 최소값을 얻을수 있는 min함수를 이용해 보자.)

a = {'A':90, 'B':80, 'C':70}
min_val = min(a.values())
print(min_val)