class Calc:
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

sum1 = Calc()
sum1.setData(10, 3)
print(sum1.add())
print(sum1.sub())
print(sum1.mul())
print(sum1.div())