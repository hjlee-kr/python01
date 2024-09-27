import time

# 매개변수 숫자가 정해지지 않았을때
# *args - 일반자료형, **kwargs - key,value로 이루어진 자료형
def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행 시간: %f 초" % (end - start))
        return result
    return wrapper

@elapsed
def myfunc(msg):
    print("'%s'을 출력합니다." % msg)

myfunc("You need python") # wrapper()

@elapsed
def myfunc2(*args, **kwargs):
    print(args)
    print(kwargs)

myfunc2(1,2,3, name='too', age=30)

# 주의할 사항
# wrapper(*args, **kwargs)
# 매개변수의 순서는 지켜야 한다.
# value값만 있는것이 앞에, key=value로 되어있는 값은 뒤에
# 입력값이 없는것은 관계없다.

# myfunc2(1,2, name='too', age=30, 3) # Error 발생
