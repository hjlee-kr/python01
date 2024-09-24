# *args
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

print(add_mul('add', 1,2,3,4))
print(add_mul('mul', 1,2,3,4))
