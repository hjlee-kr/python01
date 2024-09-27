import re

p = re.compile('[a-z]+') # 소문자 한글자 이상

# 정규표현식이 맞을때 match객체 리턴
m = p.match("python")
print(m)
# 맞지 않는다 None 리턴
m = p.match("3python")
print(m)

p = re.compile('[a-z]+')
m = p.match('python')
if m:
    print("Match found: ", m.group())
else:
    print('no match')
