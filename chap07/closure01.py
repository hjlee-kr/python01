# 클로저
# 파이썬은 함수안에 함수를 구현할 수 있다.
# 클로저는 함수안에 구현 함수를 리턴하는 것을 의미

'''
class Mul:
    def __init__(self, m):
        self.m = m
    def mul(self, n):
        return self.m * n

if __name__ == "__main__": # 이 파일에서 시작될 때만 처리
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3.mul(10))
    print(mul5.mul(10))
'''
'''
class Mul:
    def __init__(self, m):
        self.m = m
    def __call__(self, n):
        # 함수이름을 __call__ 로 만들면
        # 객체변수이름으로 함수를 호출할 수 있다.
        return self.m * n
    
if __name__ == "__main__": # 이 파일에서 시작될 때만 처리
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10)) # __call__(10) 이 실행
    print(mul5(10))
'''

def mul(m):
    def wrapper(n):
        return m * n
    return wrapper  # 클로저

if __name__ == "__main__": # 이 파일에서 시작될 때만 처리
    mul3 = mul(3) # wrapper(n) - m=3으로 세팅
    mul5 = mul(5) # wrapper(n) - m=5으로 세팅

    print(mul3(10)) # wrapper(10) 이 실행
    print(mul5(10))