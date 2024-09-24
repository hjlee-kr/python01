a = 1 #전역변수
def vartest(a):
    a = a + 1 #지역변수

vartest(a)
print(a)
# print(a)의 출력값은? 1

# 전역변수 a값을 변경시키려면
# a값을 넘겨주것을 사용하고 결과를 리턴받아서 처리
# 함수내에서 global a로 선언하고 사용하여야 한다.

def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)

def vartest():
    global a #전역변수를 지역에서 사용하도록 만든다.
    a = a + 1

vartest()
print(a)