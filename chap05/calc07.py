class Calc:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class safeCalc(Calc):
    # 메서드 오버라이딩 : 부모클래스의 메서드를
    # 상속받은 클래스가 새로 정의하여 사용하는 것
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
sum1 = safeCalc(4, 0)
print(sum1.add())
print(sum1.sub())
print(sum1.mul())
print(sum1.div())

