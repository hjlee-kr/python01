# 우리가 일반적으로 알고 있는상식
# 함수의 리턴값은 하나다!!!
# python도 이법칙에서 벗어나지 않는다.

def add_and_mul(num1, num2):
    return num1+num2, num1*num2 # tuple형태로 리턴된다.

result = add_and_mul(3,4)
print(result)

#(7, 12)
