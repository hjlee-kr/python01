import re

# 정규식 그룹의 그룹이름 지정 - ?P<name> 사용
# 사용예) (\w+) -> (?P<name>\w+)
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search('park 010-1234-1234')
print(m.group('name'))
