# 문자열 포매팅 2
# format() 함수 사용
str1 = "I eat {0} apples".format(5)
str2 = "I eat {0} apples".format("five")
print(str1)
print(str2)
str1 = "i eat {0} apple. so was sick for {1} days".format(10, "three")
print(str1)
str1 = "i eat {num1} apple. so was sick for {num2} days".format(num1=10, num2="three")
print(str1)