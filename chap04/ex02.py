# Q2. 모든 입력의 평균값 구하기
def avg_number(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_number(1,2,3,4,5))
print(avg_number(11,22,33,44,55))