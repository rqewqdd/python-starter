# [문제4] 혈액형
#
# 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다.
#
# ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# for 문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.

blood = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

ablood = 0
bblood = 0
oblood = 0
abblood = 0

for ads in blood:
    if ads == 'A':
        ablood += 1
    elif ads == 'B':
        bblood += 1
    elif ads == 'O':
        oblood += 1
    elif ads == 'AB':
        abblood +=1
print(ablood)