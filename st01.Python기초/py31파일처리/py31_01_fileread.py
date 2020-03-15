

#########################
# readline() 파일에서 한 줄씩 읽기
print("readline() 파일에서 한줄씩 읽기")
ptr = open(".\\st01.Python기초\\py31파일처리\\file\\phones.txt",
           "r", encoding="UTF-8")
s = ptr.readline()  # 한 줄 읽기
print(s, end="")  # 모니터의 출력
s = ptr.readline()  # 한 줄 읽기
print(s, end="")  # 모니터의 출력
s = ptr.readline()  # 한 줄 읽기
print(s, end="")  # 모니터의 출력
ptr.close()  # 파일 닫기
#########################
##
# 반복문으로 처리
print("readline() 파일에서 한줄씩 읽기")
ptr = open(".\\st01.Python기초\\py31파일처리\\file\\phones.txt",
           "r", encoding="UTF-8")
line = ptr.readline()

while line != "":
    # 모니터 출력
    print(line, end="")
    # 다시 파일에서 읽기
    line = ptr.readline()
#########################
##
