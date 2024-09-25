# python class
"""
class 클래스이름:
    클래스 내용

상속
class 클래스이름(부모클래스):
    클래스 내용

생성자
class 클래스이름:
    def __init__(self): # self는 클래스객체를 의미
        생성자내용        
"""
class Family:
    lastname = "김"
    # 클래스변수 -> 클래스이름으로 불러올수 있다. 
    # 클래스가 만들어질때 존재
    # 클래스변수는 어떤객체든 값을 변경하면 모든 객체의 
    # 클래스변수값이 변경됩니다.
    # 주소값을 모든 객체가 공유하고 있다.(같은주소를 가르킨다.)
    def __init__(self):
        self.firstname = "유신" # 객체변수 -> 객체가 생성될때 만들어진다.

print(Family.lastname)
a = Family()
print(a.lastname)
print(Family.lastname)
print(a.firstname)
# print(Family.firstname)

a = Family()
b = Family()
Family.lastname="박"
print(a.lastname)
print(b.lastname)

a = Family()
b = Family()
a.lastname="박"
print(a.lastname)
print(b.lastname)

a = Family()
b = Family()
a.firstname="길동"
print(a.firstname)
print(b.firstname)