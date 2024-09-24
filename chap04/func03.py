# 함수의 사용예
# 매개변수를 지정해서 처리하는 방법
def add(num1, num2):
    return num1 + num2

# 매개변수를 지정해서 사용할 때는 순서를 바꿔서 사용할 수 있다.
result = add(num2 = 5, num1 = 7)
print(result)