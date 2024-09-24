"""
for 문
 # 다른프로그램에서 사용하는 향상된 for문을 기본으로 한다.
for 변수 in 리스트or튜플or문자열:
    수행할 문장(처리문)
    수행할 문장
    ...
for문이 끝난후 처리
"""
list1 = ['one', 'two', 'three']
for i in list1:
    print(i)
print("프로그램종료")

str1 = "Life is too short"
for i in str1: # 인덱싱의 기준으로 가져온다.
    print(i)
print("프로그램종료")

list1 = [(1,2), (3,4), (5,6)]
for (first, last) in list1:
    print("%d + %d = %d" %(first, last,first + last))

print("프로그램종료")