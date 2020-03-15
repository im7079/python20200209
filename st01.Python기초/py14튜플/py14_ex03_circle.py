# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성하여 본다.
# 예시)
# 원의 반지름을 입력하시오: 10
# 원의 넓이는 314.1592653589793 이고
# 원의 둘레는 62.83185307179586 이다.
import math  # PI=3.14159...변수를 사용하기 위해서 import


def circle(radius):
    면적 = math.pi * radius**2
    둘레 = 2 * math.pi * radius
    return(면적, 둘레)


def main():
    str = input("원의 반지름을 입력하시오:")
    radius = float(str)  # 문자열을 실수로 형변환
    # 원의 넓이와 둘레를 계산 한다.
    (x, y) = circle(radius)  # x=면적, y=둘레
    tmp = "원의 넓이는 %10.4f, 둘레는 %10.4f 이다" % (x, y)
    print(tmp)


# main 함수 호출
if __name__ == "__main__":
    main()
