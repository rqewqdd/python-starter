def solution(phone_number):
    answer = "*"*(len(phone_number)-4)+phone_number[-4:]
    return answer

# 결과물
phone_number = "01012345678"
print(solution(phone_number))

# 다른풀이
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
