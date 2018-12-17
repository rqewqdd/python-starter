# [문제3] 구구단 출력
#
# 입력을 자연수 n(2부터 9까지의 자연수)으로 받았을 때, n에 해당되는 구구단을 출력하는 함수를 작성해 보자.

def dan(val):
    for i in range(1,10):
        print(val,'*',i,'=',val*i)

gugudan = int(input())
dan(gugudan)
