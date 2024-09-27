import re

# 문자열의 숫자를 hex값으로 변경해주는 프로그램
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
result = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code')
print(result)