# 주민번호의 뒷자리를 *로 바꾸는 프로그램
data = """
park 800905-1049118
kim 700905-1059119
"""
print(data) # 원 데이터

"""
result = []
for line in data.split("\n"): # 한줄씩 나누기
    word_result = []
    for word in line.split(" "): # 공백으로 나누기
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + '-' + "*******" # word[:7] + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result)) # 변경데이터
"""
# 간결하게 바꿀수 있는것이 정규표현식

import re #정규표현식을 사용하기 위한 모듈

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
