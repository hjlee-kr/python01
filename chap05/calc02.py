result1 = 0 # 결과값 보관변수 선언
result2 = 0 # 결과값 보관변수 선언
# 들어온 값을 더해서 누적하는 함수
def add1(num):
    global result1
    result1 += num # 입력값 더하기
    return result1 # 결과 리턴
def add2(num):
    global result2
    result2 += num # 입력값 더하기
    return result2 # 결과 리턴

print(add1(3))
print(add1(7))

print(add2(4))
print(add2(9))