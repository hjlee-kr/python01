# datetime.date()
# 연,월,일로 날짜를 표현할 때 사용합니다.
import datetime
day1 = datetime.date(2024, 9, 25)
day2 = datetime.date(2024, 12, 31)

print(day1)
print(day2)

diff = day2 - day1
print("%s일  남았습니다" % diff.days)

# 시간과 관련된 모듈
import time
# 1970년 1월 1일 0시 0분 0초를 기준으로 한 시간(단위:초)
print(time.time())
# 초단위 시간(time.time())을 연,월,일,시,분,초 형태로 바꾸어준다.
print(time.localtime(time.time()))
# time.localtime()에서 리턴된값을 문자열로 바꿔준다.
print(time.asctime(time.localtime(time.time())))
# 현재시간을 문자열형태로 보여준다.
print(time.ctime())
# time.strftime()
# 시간에 관련된 내용을 표시할 수 있도록 여러가지 포맷을 제공
# time.strftime('출력할 포맷', time.localtime(time.time()))
"""
시간에 관련된 포맷 (점프투파이썬 P260 참고)
%b - 달의 줄임말 - Jan
%x - 월/일/년
%Y - 연도출력 4자리
%y - 연도출력 2자리
%m - 달 - 숫자로
%d - 일 - 숫자로
%M - 분
%H - 시간 - 24시간형태
%I - 시간 - 12시간형태
%p - AM/PM
"""
print(time.strftime('%x', time.localtime(time.time())))
# 09/25/24
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
# 2024-09-25


# time.sleep(숫자) - 시간딜레이를 준다. 단위는 초
for i in range(10):
    print(i)
#    time.sleep(2)
print("sleep() - 프로그램종료")


import math
# math.gcd() - 최대공약수
print(math.gcd(60, 100, 80))

# math.lcm() - 최소공배수
print(math.lcm(60, 100, 80))

import random
# random.random() - 난수를 리턴
print(random.random()) # 0.0~1.0사이의 실수를 리턴
print(random.randint(1, 45)) # 1~45사이의 정수를 리턴

import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']
# itertools.zip_longest() 두개의 자료를 쌍으로 묶는 함수
result = itertools.zip_longest(students, snacks, fillvalue="새우깡")
print(list(result))

# 경우의 수(순열)
result = list(itertools.permutations(['1','2','3'], 2))
print(result)

# 조합
result = list(itertools.combinations(['1','2','3'], 2))
print(result)

# 로또 경우의 수
#result = len(list(itertools.combinations(range(1,46), 6)))
#print(result)

# functools.reduce()
def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1,2,3,4,5]
result = add(data)
print(result)

import functools
data = [1,2,3,4,5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)
# ((((1 + 2) + 3) + 4) + 5)

# 최대값 구하기
data = [3, 2, 8, 1, 6, 7]
result = functools.reduce(lambda x, y: x if x > y else y, data)
print(result)

# operator 패키지안의 itemgetter()를 사용하기 위한 선언
from operator import itemgetter

students = [
    ('jane', 22, 'A'),
    ('dave', 32, 'B'),
    ('sally', 17, 'B')
]

# 리스트안의 튜플에서 index 1번인 나이로 정렬
result = sorted(students, key=itemgetter(1))
print(result)

students =[
    {"name":"jane", "age": 22, "grade": "A"},
    {"name":"dave", "age": 32, "grade": "B"},
    {"name":"sally", "age": 17, "grade": "B"}
]
# 리스트안의 딕셔너리에서 age키값으로 정렬
result = sorted(students, key=itemgetter("age"))
print(result)

from operator import attrgetter
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('jane',22,'A'),
    Student('dave',32,'B'),
    Student('sally',17,'B')
]
# attrgetter 클래스 안의 변수이름으로 정렬할때 사용
result = sorted(students, key=attrgetter('age'))
for std in result:
    print(std.name, std.age, std.grade)

# shutil - 파일을 복사하거나 이동할 때 사용합니다.
# import shutil
# shutil.copy("test.txt", "test2.txt")
# shutil.move("test2.txt", "chap05-5/test2.txt")


# glob - 디렉토리안의 파일검색
import glob
result = glob.glob("D:\hjlee\workspaces\python01\chap04\ex*")
print(result)

# pickle - file과 함께 쓰이는데 반드시 binary 모드로 사용
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'java'}
pickle.dump(data, f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
f.close()
print(data)
