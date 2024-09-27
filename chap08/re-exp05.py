import re
# ^는 처음시작이라는 의미이지만
# re.MULTILINE과 함께 쓰이면, 각줄의 처음이라는 의미로 변경됨
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))