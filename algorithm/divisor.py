def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer

# 결과물
arr = [1,2,3,4,6]
print(solution(arr,5))

# append() : list 요소 추가
# sort() : list 요소 정렬


# 다른풀이

def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]
