import random

#def random_pop(data):
#    number = random.randint(0, len(data) - 1)
#    return data.pop(number)
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))


data = [1,2,3,4,5]
print(data)
data = random.sample(data, len(data))
print(data)

# 로또 번호 수집
data = list(range(1,46))
print(data)
data = random.sample(data, 6)
print(data)

