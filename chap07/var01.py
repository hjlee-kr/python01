# 파이썬은 동적언어
# 변수 타입이 값이 넣어질때 결정된다.

def add(a:int, b:int) -> int:
    return a + b
# 변수 옆에 :과 type을 적는것 - 타입 어노테이션
# 타입어노테이션은 타입에 대한 결정이 아니고 권고 이다.
print(add(3, 4.6))

# 잘못된 형식의 변수를 사용할 때 Error로 만들고 싶을때는
# mypy 라이브러리를 사용하면 됩니다.
# pip install mypy