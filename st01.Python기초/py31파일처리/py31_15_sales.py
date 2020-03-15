# 입력 파일 이름과 출력 파일 이름을 받는다.

# 입력과 출력을 위한 파일을 연다.

# 합계와 횟수를 위한 변수를 정의한다.

# 입력 파일에서 한 줄을 읽어서 합계를 계산한다.

# 총매출과 일평균 매출을 출력 파일에 기록한다.

ptr = open(
    "C:\\python 20200209\\Python기초.20200209.실습용\\st01.Python기초\\py31파일처리\\file\\sales.txt", "r")


line = ptr.readline()
sum1 = 0
avg = 0
# 파일에서 읽기
line = ptr.readline()
count = 1
while line != "":
    # 모니터 출력
    print(line, end="")

    line1 = int(line)
    sum1 = line1 + sum1

    # 파일에서 읽기
    line = ptr.readline()
    count = count + 1

ptr.close()


ptw = open(
    "C:\\python 20200209\\Python기초.20200209.실습용\\st01.Python기초\\py31파일처리\\file\\summary.txt", "a", encoding="UTF-8")

str1 = "합계" + str(sum1)
ptw.write(str1)
ptw.write("\n")
avg = sum1 / count
str1 = "평균" + str(avg)
ptw.write(str1)
ptw.write("\n")

ptw.close()
