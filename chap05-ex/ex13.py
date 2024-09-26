# Q13. 누나는 영철이보다 며칠 더 먼저 태어났을까?
import datetime  # datetime 모듈을 임포트하여 날짜 및 시간 관련 기능 사용

# 두 날짜를 설정
day1 = datetime.date(1995, 12, 20)  # 첫 번째 날짜: 1995년 12월 20일
day2 = datetime.date(1998, 10, 6)   # 두 번째 날짜: 1998년 10월 6일

# 두 날짜의 차이를 계산
result = day2 - day1  # result는 두 날짜의 차이를 나타내는 timedelta 객체

# 차이의 일수 출력
print(result.days)  # 출력: 1032 (1995년 12월 20일부터 1998년 10월 6일까지의 일수)