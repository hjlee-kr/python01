# 문자열 인덱싱 & 슬라이싱
# 문자열로 저장하면 자동으로 인덱싱
# 시작은 0부터이다. 오른쪽은 하나씩증가, 왼쪽은 하나씩감소
str1 = "Life is too short, You need python."
print(str1[3])
print(str1[-3])
# 슬라이싱 - 문자열을 자르는것
print(str1[0:6]) # str1의 0이상 6미만 -> 0부터 5까지 
print(str1[:6]) # 위의 명령과 동일한 의미 : 처음부터 5까지
print(str1[8:]) # 8부터 끝까지 보여주세요
print(str1[19:-7])