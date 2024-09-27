# 문자열 바꾸기 (정규식과 매치되는 부분)
import re

p = re.compile("(blue|white|red)")
result = p.sub("colour", "blue socks and red shoes")
# "blue socks and red shoes" 에서 정규표현식과 맞는 문자열을
# colour 로 변경하세요
print(result)

# 앞에 있는 하나만 바꾸고 싶을때 count값을 줍니다.
result = p.sub("colour", "blue socks and red shoes", count = 1)
print(result)

result = p.subn("colour", "blue socks and red shoes")
print(result)
result = p.subn("colour", "blue socks and red shoes", count = 1)
print(result)
