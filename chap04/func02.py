# 함수의 형태
# 4가지
"""
1. 리턴도있고 입력값도 있고
2. 리턴만 있는것
3. 입력값만 있는것
4. 입력값 리턴 모도 없는 함수
"""
# 1
def add(num1, num2):
    return num1 + num2
# 2
def strout():
    return "strout"
# 3
def add_2 (num1, num2):
    print("%d + %d = %d" %(num1, num2, num1+num2))
# 4
def show():
    print("hello python")

print(strout())
add_2(3, 5)
show() 