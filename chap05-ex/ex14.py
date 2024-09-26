# Q14. 기록순으로 정렬하기
import operator

data = [('윤서현', 15.25),
        ('김예지', 13.31),
        ('박예원', 15.34),
        ('송순자', 15.57),
        ('김시우', 15.48),
        ('배숙자', 17.9),
        ('전정웅', 13.39),
        ('김혜진', 16.63),
        ('최보람', 17.14),
        ('한지영', 14.48),
        ('이성호', 17.7),
        ('김옥순', 16.71),
        ('황민지', 17.65),
        ('김영철', 16.7),
        ('주병철', 15.67),
        ('박상현', 14.16),
        ('김영순', 14.81),
        ('오지아', 15.13),
        ('윤지은', 16.93),
        ('문재호', 16.39)
        ]
# itemgetter(num) - num은 자료의 index를 의미한다.
data = sorted(data, key=operator.itemgetter(1))
for d in data:
    print(d)