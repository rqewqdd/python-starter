# 딕셔너리 값 추출2
#
# 다음은 딕셔너리의 a에서 'C'라는 key에 해당되는 value를 출력하는 프로그램이다.
#
# >>> a = {'A':90, 'B':80}
# >>> a['C']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'C'
# a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생하게 된다. 'C'에 해당되는 키값이 없을 경우 오류 대신 70을 얻을수 있도록 수정해 보자.

a = {'A':90,'B':80}
a.get('C',70)

# get(x) 함수는 x라는 key에 대응되는 value를 돌려준다.