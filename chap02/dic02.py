# 딕셔너리 값 추가, 삭제 (쌍으로 이루어진다.)
dic1 = {1:"lee", 2:"kim", 3:"park"}
print(dic1)
dic1[4] = "song"
print(dic1)
dic1['name'] = "hj"
print(dic1)
# 삭제 - key값으로 삭제합니다.
del dic1[3]
print(dic1)
del dic1['name']
print(dic1)
# 딕셔너리는 중복되는 key값을 허용하지 않는다.
# 같은 키값으로 값을 입력하면 어떻게 될까요?
dic1 = {1: 'lee', 2: 'kim', 4: 'song'}
dic1[1] = 'park'
print(dic1) # error를 발생시키지는 않는다. 기존값을 덮어쓴다.