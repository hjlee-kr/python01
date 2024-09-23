# 문자열 포매팅 3
# %10s 의미는 공간을 10개에 문자 or 숫자 오른쪽 정렬
str1 = "%10s, python" % "Hi"
print(str1)
# %-10s : 왼쪽정렬
str1 = "%-10s, python" % "Hi"
print(str1)
num1 = 35
num2 = 3.14159
str1 = "%10d" % num1
print(str1)
str1 = "%0.2f" % num2 # .2 로 포매팅하면 소수점 2자리로 표현하라는 의미
print(str1)
# format()를 사용하여 정렬하는 방법
str1 = "{0:<10}, python".format("hi") # 공간10개를 만들고 왼쪽정렬
print(str1)
str1 = "{0:>10}, python".format("hi") # 공간10개를 만들고 오른쪽정렬
print(str1)
str1 = "{0:^10}, python".format("hi") # 공간10개를 만들고 가운데정렬
print(str1)
str1 = "{0:=^10}, python".format("hi") # 공간10개를 만들고 가운데정렬후 빈공백은 =로 채운다.
print(str1)
str1 = "{0:>0.2f}".format(3.14159) # 소수점 자리수 제한
print(str1)