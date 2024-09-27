import re

p = re.compile('a.b') # 첫번째: a, 두번째: 모든문자(\n제외), 세번째:b
m = p.match('a\nb')
print(m)

# \n도 .에 포함시키도 싶다.
# re.DOTALL 옵션을 사용하면 된다.
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
