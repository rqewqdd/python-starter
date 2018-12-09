# [문제5] 조건문3
#
# 다음 코드의 결과값은 무엇일까?

a = "Life is too short, you need python"
if 'wife' in a:  # a안에 wife가 포함되어있는 경우
    print('wife')
elif 'python' in a and 'you' not in a:  # a안에 python 포함되어 있고 you가 포함되어있지 않은경우
    print('python')
elif 'shirt' not in a:  # a안에 shirt 포함되어있지 않은 경우
    print('shirt')
elif 'need' in a:  # a안에 need가 포함되어있는 경우
    print('need')
else:              # 전부 아닌경우
    print('none')