# command 창에서 사용할 수 있는 메모장
# 쓰기, 읽기
# 한가지 메모만 기록하고 읽을 수 있도록
# memo.py 모드 내용
# 모드: -w:새로쓰기, -a:추가하기, -r:읽기
# 내용: 문자열로 입력합니다.
import sys

mode = sys.argv[1]
if mode == '-w': # 새로쓰기
    memo = sys.argv[2]
    with open('meme.txt', 'w', encoding='utf-8') as f:
        f.write(memo)
        f.write('\n')
elif mode == '-a': # 추가
    memo = sys.argv[2]
    with open('meme.txt', 'a', encoding='utf-8') as f:
        f.write(memo)
        f.write('\n')
elif mode == '-r': # 읽기
    with open('meme.txt', 'r', encoding='utf-8') as f:
        memo = f.read()
        print(memo)
else:
    print("모드를 잘못입력하셨습니다.")

# print(mode)
# print(memo)
print("프로그램종료")