# 입력값의 갯수를 모를때 사용하는 방법 (*변수이름)
def add_all(*args):
    result = 0
    print(type(args))
    for i in args:
        result += i
    return result

result = add_all(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(result)
