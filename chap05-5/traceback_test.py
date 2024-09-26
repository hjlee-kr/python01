# 발생한 오류 추적에 유용한 모듈 traceback
# 예외처리와 함께 쓰인다.
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())
        # java에서 e.printStackTrace() 와 같은역할

main()