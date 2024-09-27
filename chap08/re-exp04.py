import re

# re.I는 대소문자 구별없이 수행
p = re.compile('[a-z]+', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))
