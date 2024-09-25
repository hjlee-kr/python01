class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError() # raise 는 강제로 예외를 만들어주는 예약어
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print("허용하지 않는 별명입니다.")
