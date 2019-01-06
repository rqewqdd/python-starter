def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    return ''.join(answer)

# 결과물

s = "Zbcdefg"
print(solution(s))

# sort(reverse=True) : 내림차순
# ''.join() : '' 구분자를 통해 리스트를 문자열로 변환

# 다른풀이

def solution(s):
    return ''.join(sorted(s, reverse=True))

