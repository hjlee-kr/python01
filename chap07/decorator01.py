# 데코레이터
"""
import time

def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수 수행시간 : %f 초" % (end - start))


myfunc()
"""
"""
import time

# 함수를 바꾸지 않고 기능을 추가할 수 있도록
# 만드는 클로저(함수)를 "데코레이터"라고 합니다.
def elapsed(original_func):         # 함수를 입력값을 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 함수 실행
        end = time.time()
        print("함수 수행시간 : %f 초" % (end - start))
        return result               # 함수 결과 리턴
    return wrapper

def myfunc():
    print("함수가 실행됩니다.")

decorated_myfunc = elapsed(myfunc) # wrapper() 로 지정
decorated_myfunc()          # wrapper() 실행
"""

import time

# 함수를 바꾸지 않고 기능을 추가할 수 있도록
# 만드는 클로저(함수)를 "데코레이터"라고 합니다.
def elapsed(original_func):         # 함수를 입력값을 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 함수 실행
        end = time.time()
        print("함수 수행시간 : %f 초" % (end - start))
        return result               # 함수 결과 리턴
    return wrapper

@elapsed # myfunc이 데코레이터로 elapsed를 사용하겠다는 의미
def myfunc():
    print("함수가 실행됩니다.")
@elapsed
def myfunc2():
    print("함수를 추가실행합니다.")

myfunc()
myfunc2()
