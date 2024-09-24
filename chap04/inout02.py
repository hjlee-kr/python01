# print() 함수에 대해서 알아보자.
# 1
print("life" "is" "too" "short")
# 2
print("life"+"is"+"too"+"short")
# 1,2의 처리결과는 동일합니다.
# 3 : 문자열을 ,로 구분하여 입력하면 문자열 출력시 한칸씩 띄어서 출력
print("life","is","too","short")
# print함수를 줄변경 안하고 사용하기 end="" 지정
for i in range(1,11):
    print(i, end=" ")
print()    
print("프로그램종료")
