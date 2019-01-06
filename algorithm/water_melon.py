def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer

# 결과물
print(solution(3))

# range() : 범위

# 다른풀이

def water_melon(n):
    s = "수박" * n
    return s[:n]
