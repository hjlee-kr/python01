class MyError(Exception):
    def __str__(self):
        return "허용하지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError() # raise 는 강제로 예외를 만들어주는 예약어
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e) # 허용하지 않는 별명입니다.
