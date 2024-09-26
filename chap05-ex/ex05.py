# Q5. 16진수를 10진수로 변경하기
data = hex(234)
print(data)
print(type(data))

data_int = int(data, 16) # 16진수로 표시되어있는 문자열data를 int로 변경
print(data_int)