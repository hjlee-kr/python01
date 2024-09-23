a = dict()
print(a)
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' # Error
a[250] = 'python'
print(a)
# 딕셔너리의 key값으로 변할 수 있는 값은 사용할 수 없다.(mutable객체사용불가)