#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오 
# 한행씩 읽어 들이기
# readline() 함수 사용
# 파일로 데이터 입력 후 이를 화면에 출력하는 프로그램

ptr = open(".\\file\\proverbs.txt", "r", encoding="UTF-8")
line = ptr.readline()

while line != "":
    #모니터 출력
    print(line, end="")
    #다시 파일에서 읽기
    line = ptr.readline()

import os.path

outfile = open(".\\file\\output.txt", "w")

if os.path.isfile(".\\file\\proverbs.txt"):
    outfile.write()
    outfile.write("김철수 010-1234-5679")
    outfile.write("김영희 010-1234-5670")

outfile.close()

