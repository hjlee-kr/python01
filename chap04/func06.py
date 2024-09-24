# key = vlaue를 입력값으로 넘길 수 있습니다.
def print_kwargs(**kwargs):
    print(kwargs)

# key는 문자열로 입력된다. 
# key입력시 ''나 ""는 사용하지 않는다.
print_kwargs(name='kim', age=30)