i  = input("시작단 입력")  # 문자열
i = int(i)  # 문자열을 정수로 변경
j = input("종료단 입력")  # 문장열
j = int(j)  # 문자열을 정수로 변경

if i < j:
    # 값을 변경
    temp = i
    i = j
    j = temp

else:
    pass

for x in range(temp, 20, 1):
    for y in range(1, 10, 1):
        str = "%2s*%s=%3s" % (x, y, x*y)
        if y == 9:
            print(str, end=".")
        else:
            print(str, end=",")
    print()

