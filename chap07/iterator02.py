# 클래스에서 __iter__()함수가 구현되어있으면
# 반드시 __next__()함수가 있어야 한다.
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration  # raise : 예외를 강제로 만들어주는 예약어
        result = self.data[self.position]
        self.position += 1
        return result
    
if __name__ == "__main__":
    i = MyIterator([1,2,3])
    #for item in i:
    #    print(item)
    print(i.__next__())
    print(i.__next__())
    print(i.__next__())
    print(i.__next__()) # Error발생

