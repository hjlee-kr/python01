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

sum1 = Calc(3,10)
print(sum1.add())
print(sum1.sub())
print(sum1.mul())
print(sum1.div())