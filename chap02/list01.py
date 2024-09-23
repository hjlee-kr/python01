# 리스트 자료형
list01 = [1,2,3,4,5,6,7,8,9]
print(list01)
list01 = ["Lee", "Kim", "Park", "Jung", "Song", "You"]
print(list01)
# python 에는 다른 type의 자료형도 리스트에 같이 담을 수 있다.
list01 = [1, 2, 3, "one", "two", "three"]
print(list01)
# 리스트안에 리스트를 담을 수도 있다.
list01 = [1, 2, 3, [1,2,3]]
print(list01)
# 리스트의 인덱싱
print(list01[0])
print(list01[1])
print(list01[2])
print(list01[3])
print(list01[3][0])
print(list01[-1][0])
# 리스트의 슬라이싱
print(list01[0:3])
print(list01[:3])
print(list01[2:])
# 문제: 아래 list01에서 2,3만 뽑아내서 list02에 담고 출력
list01 = [1,2,3,4,5]
list02 = list01[1:3]
print(list02)