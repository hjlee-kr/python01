# Q2. 클래스 상속받고 메서드 추가하기 2
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

# 메서드 오버라이딩 - 부모클래스의 메서드를 재정의
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)