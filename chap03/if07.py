"""
if문정리

if 조건문:
    처리문
elif 조건문:
    처리문 or pass
elif 조건문:
    처리문
...
else:
    처리문

처리문 하나일때는
if 조건문: 처리문   으로 사용할수 있다.

python에서 삼항연산자를 대치해서 사용하는 방법
참일때 처리문 if 참인조건 else 거짓일때 처리문
"""
score = 50
if score >= 60:
    message = "pass"
else:
    message = "fail"
print(message)

message = "pass" if score >= 60 else "fail"
print(message)
