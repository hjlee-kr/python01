import re

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# () 묶어주는 것을 그룹화 라고 합니다.
m = p.search('park 010-1234-1234')
print(m.group(0)) # 정규식과 전체 매치되는 값을 리턴
print(m.group(1)) # 정규식의 첫번째 그룹과 매치되는 값을 리턴
print(m.group(2)) # 정규식과 두번째 그룹과 매치되는 값을 리턴
print(m.group(3))