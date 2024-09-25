# abs() - 절대값 리턴 
print(abs(-7)) # 7

# all() - 반복 데이터에서 모든요소가 참일때 True 리턴 
print(all([1,2,3,4,0])) # False
print(all([])) # True -> 특이한 케이스

# any() - 반복 데이터에서 하나의 요소가 참이면 True 리턴
print(any([1,2,3,4,0])) # True
print(any([])) # False

# chr() - 숫자값을 입력받아 문자로 변경
print(chr(65)) # A
print(chr(44032)) # 가

# dir() - 객체가 지닌 변수, 함수를 보여주는 메서드
print(dir([1,2,3])) 

# divmod() - 숫자를 2개를 받아서 (몫,나머지) 를 tuple형태로 리턴
print(divmod(10,3)) # (3, 1)

# enumerate() - 순서가 있는 데이터를 입력받아 인덱스 값을 포함하여 리턴
for index, value in enumerate(['body', 'foo', 'bar']):
    print(index, value)

# eval() - 문자열로 되어있는 수식을 계산해주는 함수
print(eval("3 + 4"))
print(eval("divmod(10,3)"))

# filter()
#def positive(x):
#    result = []
#    for i in x:
#        if i > 0:
#            result.append(i)
#    return result
#print(positive([1, -3, 2, 5, 0, -6, 7, 10]))
def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 5, 0, -6, 7, 10])))

# hex() - 정수를 입력받아 16진수로 변경
print(hex(50))

# id() - 객체의 주소값을 리턴
a = 3
print(id(a))
print(id(3))

# input() 키보드에서 입력받는 함수 (\n)이 들어올때 까지 수집
# input("알림메시지")
# input() 으로 받는 데이터는 str 타입입니다.
# num = int(input("숫자를 입력하세요: "))

# int() 문자형숫자 or float 자료를 정수로 리턴
print(int("3"))
print(int(3.14))
print(int("11", 2)) # 2진수 11을 int로 리턴, 3
print(int("1F", 16)) # 16진수 0x1F를 int로 리턴, 31

# isinstace(object, class) - 객체가 이 클래스인지?
class Person: pass
a = Person()
print(isinstance(a, Person)) # True
b = 3
print(isinstance(b, Person)) # False

# len() - 입력값의 길이 (요소의 갯수)
print(len("I love you")) # 10
print(len([1, 2, "you", 4])) # 4
print(len((1,2,3,4))) #4

# list() - 반복가능한 데이터 리스트로 만들어주는 함수
# index으로 리스트화 합니다.
result = list("Python") # 문자열 -> 리스트
print(result)
result = list((1,2,"you")) # 튜플 -> 리스트
print(result)

# map() - 반복가능한 데이터를 모든 요소에 적용
# def two_times(numberList):
#    result = []
#    for number in numberList:
#        result.append(number * 2)
#    return result
#result = two_times([1,2,3,4])
#print(result) # [2,4,6,8]

def two_times(x):
    return x * 2
result = list(map(two_times, [1,2,3,4]))
print(result)


# max() - 반복가능한 데이터중 가장 큰 값을 리턴
print(max([4,6,3,8,10,0,9])) #10
print(max("python")) #y - 문자는 아스키코드가 큰값을 리턴

# min() - 반복가능한 데이터중 가장 작은 값을 리턴
print(min([4,6,3,8,10,0,9])) #0
print(min("python")) #h

# oct() - 정수를 8진수 문자열로 리턴
print(oct(20)) #0o24 

# open(파일이름, mode)
# mode : w: 새로쓰기, r: 읽기, a: 이어쓰기(없으면새로),
# b: binary (b는 w,r,a와 같이 사용)


# ord() - 문자를 유니코드 숫자로 리턴
print(ord('A'))
print(ord("가"))

# pow(x,y) - x를 y제곱한 값을 리턴
print(pow(2,5)) # 2의 5승 = 32

# range(x) - 0부터 x-1까지
# range(x,y) - x부터 y-1까지
# range(x,y,step) - x부터 y-1까지 step 단위로
print(list(range(10)))
print(list(range(0,10)))
print(list(range(0,10,1)))


# round() - 숫자를 입력받아서 반올림해서 리턴
print(round(4.3))
print(round(4.7))
print(round(3.141592, 2)) # 소수점 2자리까지 반올림해서 보여준다.

# sorted() - 입력데이터를 정렬 리스트로 리턴
print(sorted([6,3,4,9,7,4,5]))
print(sorted("python"))
print(sorted((3,2,1)))

# str() - 입력값을 문자열 형태로 리턴
print(str(3) + "Hi")
print(str(('p', 'y', 't', 'h', 'o', 'n'))) # 넣어준 형태 그대로 저장

# sum() - 입력값을 전부 더해서 리턴
print(sum([1,2,3,4,5])) #15

# tuple() - 반복가능한데이터를 tuple 형태로 리턴
print(tuple([1,2,3,4,5]))
print(tuple("python"))

# type() - 입력값이 어떤 형태의 객체인지 리턴하는 함수
print(type("abd"))
print(type(3))
print(type(3.14))
print(type([1,2,3]))
print(type((1,2,3)))
print(type(open("test","w")))

# zip() - 동일한 갯수로 이루어진 데이터를 묶어서 리턴
result = list(zip([1,2,3], [4,5,6]))
print(result)
result = list(zip("abc", "def"))
print(result)