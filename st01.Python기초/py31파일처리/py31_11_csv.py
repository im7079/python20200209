# 엑셀 파일=> csv 파일로 저장 ==> pyhon 에서 파일 읽기 과정을 연습한다.

#########################
##
#########################


# 파일을 연다.

# 파일 안의 각 줄을 처리한다.

# 공백 문자를 없앤다.

# 줄을 출력한다.

# 줄을 쉼표로 분리한다.

# 각 줄의 필드를 출력한다.
ptw = open(
    "C:\\python 20200209\\Python기초.20200209.실습용\\st01.Python기초\\py31파일처리\\file\\data.csv", "r", encoding="UTF-8")

line = ptw.readline()
count = 1
while line != "":
    line = line.strip()
    print(line)

    list = line.split(",")
    for i in list:
        print("     ", i)

    # 파일에서 읽기
    line = ptw.readline()
    count = count + 1


ptw.close()
