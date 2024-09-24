"""
함수, 메써드, 펑션
def 함수이름(매개변수):
    수행할문장1
    수행할문장1
    ...

함수밖의 처리문

"""
# 두수를 넣으면 더한값을 리턴하는 함수
def add(num1, num2):
    return num1 + num2

num1 = 3
num2 = 4
sum = add(3,4)
print("%d + %d = %d" %(num1, num2, sum))
