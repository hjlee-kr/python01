class Calc:
    def __init__(self): # python class의 생성자
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
    
sum1 = Calc() # 클래스 사용
print(sum1.add(3))
print(sum1.add(7))
sum2 = Calc()
print(sum2.add(4))
print(sum2.add(9))