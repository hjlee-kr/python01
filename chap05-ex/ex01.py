# Q1. 클래스 상속받고 메서드 추가하기1
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator): #부모클래스를 가로안에 적는다.
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.add(20)
cal.add(4)
cal.minus(7)

print(cal.value)