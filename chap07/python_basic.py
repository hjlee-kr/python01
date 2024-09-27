# 파이썬에서 주석은 앞에 '#'을 붙이는 것
"""
여러줄 문자열에 사용하는 (""" """, ''' ''')을
이용하여 주석처럼 사용할 수 있습니다.
"""
# Hello python을 출력해보자
# 커맨드에 출력하는 함수 print()
# print() default로 마지막에 '\n' 이 포함되어있습니다.
# java println() 함수와 동일하게 출력
print("Hello python")
print("Life is too short")
# java print() 처럼 사용하려면 end='' 속성을 줍니다.
print("Helle python", end="")
print("Life is too short")
# 파이썬에서 변수를 사용할 때 "자료형선언"이 없다.
# 동적변수
a = 7       # int (정수형)
b = 7.5     # float (실수형)
c = "string"    # str
d = [1,2,3]     # list
e = (1,2,3)     # tuple
d = {'a':1, 'b':2}  # dic
# 값을 변경할 수 없는 자료형 : int, float, str, tuple
# 값을 변경할 수 있는 자료형 : list, dic
a = 7
print(id(a))
a = a + 1
print(id(a))
# 조건문
# 사용예
num1 = 10
if num1 > 10:
    # 문자포맷팅 %d:정수, %f:실수, %s:문자열
    print("%d는 10보다 큽니다." % num1)
elif num1 == 10: # java의 else if와 같은의미
    # 문자포맷팅 다른방식
    print("{}는 10과 같습니다.".format(num1))
else:
    # 문자포맷팅: 이름을 지정해서 사용
    print("{number}는 10보다 작습니다.".format(number=10))
# 파이썬에는 switch문이 없다.
# 반복문 while, for
# while
num1 = 0
while num1 < 10:
    num1 = num1 + 1  # 파이썬은 ++ or -- 같은 증감연산자가 없다.
    # num1 += 1 이런형태는 사용가능하다.
    print("%d 번 입니다." % num1)
print("while문을 빠져나갔습니다.") # while문과 동일한 column에 작성
# for
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)
print("for문을 빠져나갔습니다.")
for i in range(0, 11): # 0~10까지 i에 넣어서 for문실행
    print(i)
print("for문을 빠져나갔습니다.")
# 연산자
# +(덧셈), -(뺄셈) , *(곱셈) : 리턴값이 곱한 자료형을 따라간다.
# /(나눗셈) : 결과가 float 타입이다.
# //(나눈몫), %(나머지)
# 숫자형과 문자형을 더할수 없다.
# 1 + "hi" : 이런형태 사용불가 => str(1) + "hi" 이렇게 사용

# 함수
result = 0
def add(num1): # def 함수이름(매개변수): 리턴타입은 선언하지 않는다.
    global result # 전역변수 사용
    result += num1
    return result
# 함수는 선언만 해놓으면 아무런 동작을 하지 않는다.

print(add(3))
print(add(7))

# class

# 클래스 시작
class Calc:
    def __init__(self, num1, num2): #생성자
        self.num1 = num1    # self.num1 => 멤버변수
        self.num2 = num2    # self.num2 => 멤버변수
    def add(self):
        return self.num1 + self.num2
# 클래스 끝
cal = Calc(3, 5) # 클래스 한개 생성
print(cal.add())

# 클래스 상속
class AddCalc(Calc):
    def sub(self):
        return self.num1 - self.num2
    def div(self):
        return self.num1 / self.num2

cal = AddCalc(7, 4)
print(cal.add()) # 상속받은 함수 사용
print(cal.sub()) # 자신이 선언한 함수 사용

# 메서드 오버라이딩    
class SafeCalc(AddCalc):
    def div(self):
        if self.num2 == 0:
            return None
        else:
            return self.num1 / self.num2
        
cal = SafeCalc(4, 0)
print(cal.div())

"""
모듈 불러서 사용하기
import 파일이름[모듈] (파이썬파일 확장자없이)
사용방법은
모듈.함수()

모듈의 특정 함수만 사용하고 싶을때
from 파일이름[모듈] import 사용함수
사용방법은
사용함수() -> 함수이름으로만 사용가능
"""

# 예외처리
"""
try:
    실행문
except 에러객체 as e: # Exception 객체는 모든에러의 최상위 클래스
    print(e)
    예외상황 발생시 처리내용
else:
    예외가 없을때 처리내용
finally:
    마지막에 무조건 실행
"""

# python의 참/거짓 - 자료형에 관련된
"""
[숫자형] 0 : False, 다른숫자 : True
[문자열] "" : False, "0": True
[리스트] [] : False, [1,2,3,4]: True
[튜플]   () : False, (1,2,3,4): True
[딕셔너리] {} : False, {'name':'김'} : True
[bool] False, True :
None : False
"""

# 파일에 쓰기
f = open("test.txt", "w", encoding="utf-8") # 한글사용시 encoding적용
f.write("Life is too short.")
f.close() # open을 했으면 반드시 close()를 사용하여 닫아줍니다.

# 자동으로 close() 되는 방법
# with문을 벗어날때 자동으로 close() 됩니다.
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("Life is too short")

# 파일에 읽기
with open("test.txt", "r", encoding="utf-8") as f:
    result = f.read() # 파일 내용 전체를 가져옵니다.
    print(result)

# readline() 한 줄을 가져옵니다.
# readlines() 한 줄씩 리스트에 담는다.

# 모듈에서 설명
"""
다른 파이썬파일에서 모듈을 import하면
그안에 있는 처리문도 실행이 됩니다.
다른 파이썬파일에서 모듈 import시 
처리문이 실행되지 않게 하려면 아래와 같이 정의합니다.
if __name__ == "__main__":
    처리문1
    처리문2
    ...
"""
