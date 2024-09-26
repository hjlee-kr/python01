# 총 페이지수를 몇페이지로 할 것인지 함수를 작성
# 첫번째 인자는 전체 게시물 수,
# 두번째 인자는 한페이지에 표시할 게시물 수
# 리턴값으로 총 페이지수
def get_total_page(totalPost, perPageNum):
    if (totalPost % perPageNum == 0):
        totalPage = totalPost // perPageNum
    else:
        totalPage = totalPost // perPageNum + 1
    return totalPage

print(get_total_page(1, 10)) # 1
print(get_total_page(9, 10)) # 1
print(get_total_page(10, 10)) # 2
print(get_total_page(19, 10)) # 2
