# 문자열 포매팅
# java에서는 1 + "번" => "1번" 으로 자동변경되었지만
# python에서는 이렇게 사용할 수가 없습니다.
# %d: 정수형, %f: 실수형, %s: 문자열, %%: %출력, %o: 8진수, %x: 16진수
# 어떤 자료형인지 잘 모르겠다? : %s를 사용하세요
num1 = 1
str1 = "번 입니다"
# 방법1
str2 = "%d번 입니다." %num1
print(str2)
# 방법2
str3 = "%d%s" %(num1, str1)
print(str3)
# 방법3
str4 = "%s%s" %(num1, str1)
print(str4)
# 방법4
str5 = str(num1) + str1 # str()는 숫자형을 문자형으로 빠꿔주는 함수
print(str5)
