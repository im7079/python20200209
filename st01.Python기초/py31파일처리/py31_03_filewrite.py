# 수정사항
# 파일 열때 utp==8 인코딩 방법을 설정 하시오.
# 상대경로로 설정
# 소스에서 파일의 상대경로를 사용하고자 한다면 "open in Terminal"에 직접 실행 하여야 한다.
# >>> 터미널에서 python .\py31_03_filewrite.py 입력

import os.path

outfile = open("phones.txt", "w")

if os.path.isfile("phones.txt"):
    outfile.write("홍길동 010-1234-5678")
    outfile.write("김철수 010-1234-5679")
    outfile.write("김영희 010-1234-5670")
    print("동일한 이름의 파일이 이미 존재 합니다.")

else:
    print("동일한 이름의 파일이 이미 존재 합니다.")

outfile.close()

