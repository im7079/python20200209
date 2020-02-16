w = input("w 변의 길이 입력하세요>>") #문자열
h = input("h 변의 길이 입력하세요>>") #문자열

try:
    w= float(w) #형변환 실수
    h= float(h) #형변환 실수
except ValueError
    pass


area = w * h
primeter = 2 * (w+h)

print("사각형의 넓이:", area)
print("사각형의 둘레:", primeter)
