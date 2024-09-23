# 리스트의 연산
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# 리스트 덧셈
list3 = list1 + list2
print(list3)
# 리스크 곱셈
list3 = list1 * 3
print(list3)
# 리스트 길이? (크기)
count = len(list3)
print(count)
# 사용시 주의
# str1 = list1[0] + "번" # Error가 발생합니다.
str1 = str(list1[0]) + "번"
print(str1)

