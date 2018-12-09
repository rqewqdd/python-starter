# [문제3] 학급의 평균 점수
#
# for문을 이용하여 A 학급의 평균 점수를 구해 보자.

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
avg = 0
for i in score:
    sum += i
avg = sum / len(score)
print(avg)