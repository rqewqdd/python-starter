# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

def avg(arr):
    result = 0
    for i in arr:
        result += i
    result = result / len(arr)
    return result

# 결과물
arr = [1,2,3]
print(avg(arr))

# 다른풀이

def average(list):
    return (sum(list) / len(list))

# sum()이라는 더해주는 함수가 있다는걸 알게되었다.