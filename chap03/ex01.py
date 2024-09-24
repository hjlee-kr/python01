# 조건문의 참과 거짓
# 여러가지 조건이 있는 명령문에서 
# 참이 나오면 이후의 조건은 처리하지 않는다.
a = "Life is too short, you need python"

if "wife" in a: # False
    print("wife")
elif "python" in a and "you" not in a: # True and False => False
    print("python")
elif "shirt" not in a: # True -> 처리문실행 -> if문 빠져나옵니다.
    print("shirt")
elif "need" in a: # True -> 여기는 오지 않습니다.
    print("need")
else: # 여기도 안옵니다.
    print("none")

print("프로그램 종료")