import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (longtime_job() for i in range(5)) # 제너레이터 표현식
print(next(list_job))

# 제너레이터 표현식을 사용한 프로그램은
# 시간이 많이 걸리는 처리를 필요할 때 실행시키는데 사용합니다.
# 느긋한 계산법 (lazy evaluation)