# python 예외처리
"""
try:
    예외가 발생할 가능성이 있는 코드
except 발생오류 as 오류변수:
    예외처리
else:
    예외가 발생안되면 처리
finally:
    반드시 처리하고 넘어감
"""
try:
    a = [1,2]
    print(a[2])
#except IndexError as e:
except Exception as e: # Exception은 모든 예외의 최상위 클래스
    print(e)

print("프로그램종료")