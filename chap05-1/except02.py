try:
    age = int(input("나이를 입력하세요:"))
except Exception as e:
    print("예외발생 %s" % e)
else:
    if age >= 18:
        print("성인입니다.")
    else:
        print("미성년자입니다.")