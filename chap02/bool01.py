# Bool(불) 자료형 - java의 Boolean과 동일한 역할
# True, False : 앞글자는 대문자, 뒤에는 소문자.
a = True
b = False
print(a)
print(b)
print(type(a))
num1 = 3
num2 = 5
print(3>5)
print(3<5)
"""
Python의 참/거짓
"python" : True 
""       : False
[1,2,3]  : True
[]       : False
(1,2,3)  : True
()       : False
{"a":1}  : True
{}       : False
1        : True (0이 아닌 모든숫자)
0        : False
None     : False
"""
a = [1,2,3,4]
while a:
    print(a.pop())

print("===End===")

# bool자료형으로 변경해주는 함수 bool()
a = [1,2,3,4]
b = []
print(bool(a))
print(bool(b))





