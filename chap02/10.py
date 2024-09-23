# 문자열 관련 함수들 - 변경된 값을 리턴해서 준다.
str1 = "Life is too short"
count = str1.count("o") # o 가 몇개 있는지를 알려준다.
print(count)
num1 = str1.find("i") # 처음만나는 i를 찾아서 몇번째 있는지 알려준다.
# 만약에 존재하지 않으면 ? -1을 리턴해 줍니다.
print(num1)
num1 = str1.index("i") # 처음만나는 i를 찾아서 몇번째 있는지 알려준다.
print(num1)
# 만약에 없으면? Error가 난다.
# num1 = str1.index("v")
# print(num1)
str1 = "abcd"
str2 = ",".join(str1) # str1에 문자사이에 ,를 넣는다.
print(str2)
print("-"*50)
str1 = ['a','b','c','d'] #리스트
print(str1)
str2 = ",".join(str1)
print(str2)
# 대소문자 관련 함수
str1 = "Life is too short"
str2 = str1.upper() # 영문자 전체를 대문자로 변경
print(str2)
str2 = str1.lower() # 영문자 전체를 소문자로 변경
print(str2)
print("-"*50)
str1 = "     HI     "
str2 = ", python"
str3 = str1.lstrip() # 왼쪽 공백 제거
print(str3+str2)
str3 = str1.rstrip() # 오른쪽 공백 제거
print(str3+str2)
str3 = str1.strip() # 양쪽 공백 제거
print(str3+str2)
# 문자열 바꾸기
str1 = "Life is too short"
print(str1)
str2 = str1.replace("short", "long") # 앞의 문자열을 찾아서 뒤의 문자열로 바꾼 값을 리턴하는 함수
print(str2)
# 문자열 나누기
str1 = "Life is too short"
str2 = str1.split() # 공백을 기준으로 문자열을 나누어 줍니다.
print(str2)
str1 = "a:b:c:d"
str2 = str1.split(":") # :을 기준으로 문자열을 나눈다.
print(str2)