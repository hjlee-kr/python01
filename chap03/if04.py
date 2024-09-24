# and, or, not
money = 2000
card = True
if money >= 5000 or card: # A or B 는 A, B중 하나만 True이면 True
    print("택시를 타고 갑니다.")
else:
    print("걸어갑니다.")
print("1.프로그램종료")

if money >= 5000 and card: # A and B는 A, B가 모두 True이면 True
    print("택시를 타고 갑니다.")
else:
    print("걸어갑니다.")
print("프로그램종료")

if not card:
    print("카드가 없습니다.")
else:
    print("카드가 있습니다.")
print("프로그램종료")
