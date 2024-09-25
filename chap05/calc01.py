result = 0 # 결과값 보관변수 선언
# 들어온 값을 더해서 누적하는 함수
def add(num):
    global result
    result += num # 입력값 더하기
    return result # 결과 리턴

print(add(3))
print(add(7))