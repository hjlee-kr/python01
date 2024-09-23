# 변수를 만드는 방법
a, b = ("python", "life")
print(a)
print(b)
(a, b) = "python", "life"
print(a)
print(b)
[a, b] = ["python", "life"]
print(a)
print(b)

a = b = "python" # a,b의 id값은 같다.
# b = "python"
# a = b
print(a)
print(b)

a = 3
b = 5
# 위의 두값을 서로 맞바꾸고 싶을때
# java에서는
# temp = a
# a = b
# b = temp
print("a="+str(a))
print("b="+str(b))
a, b = b, a
print("a="+str(a))
print("b="+str(b))
# 결론은 두변수 가르키는 주소값을 교환하는 것이다.
# python의 모든 자료형은 객체이다.
# 값을 바꿀수 있는것과 없는것으로 나뉜다.
# 값을 바꿀수 있는것 => mutable
# 값을 바꿀수 없는것 => immutable
"""
===immutable 객체
bool
int
float
str
tuple
===mutable 객체
list
set
dict
"""