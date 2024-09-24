# in, not in - 리스트나 튜플안에 값이 있는지에 따라 True, False를 리턴한다.
list = [1,2,3,4,5]
if 1 in list: # if True:
    print("1이 있습니다.")
else:
    print("1이 없습니다.")
print("프로그램종료")

if 1 not in list:
    print("1이 없습니다.")
else:
    print("1이 있습니다.")
print("프로그램종료")

if 'life' in 'life is too short':
    print("life 가 있습니다.")
else:
    print("life 가 없습니다.")
print("프로그램종료")