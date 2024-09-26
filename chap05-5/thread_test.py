# 쓰레드(thread)
# : 동시에 여러가지를 처리하고 싶을때 사용한다.
# 우리가 프로그램하면 한번에 한가지만 할 수 있다.
import time
import threading # thread를 사용하기 위한 모듈

def long_task():            # 실행시간이 5초가 걸리는 함수
    for i in range(5):
        time.sleep(1)       # 1초 기다림
        print("working:%s\n" % i)

print("start")

#for i in range(5): # long_task()를 다섯번 실행하는 프로그램
#    long_task()    # 순서대로 처리함 - 총 25초 시간소요

thread = []
for i in range(5):
    t = threading.Thread(target=long_task) # 쓰레스생성
    thread.append(t)

for t in thread:
    t.start()       # 쓰레드 실행

# 쓰레드가 다 끝나고 넘어가도록 하고 싶을때 사용
for t in thread:
    t.join()

print("end")