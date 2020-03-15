# phones.txt 파일에 아래의 2줄 쓰고 저장하시오. 
# 최무선  010-1111-2222")
# 정중부  010-2222-3333
# 소스실행시 오류가 있습니다. 아래의 수정 사항을 적용하시오.
# 1. 파일 저장할때 utf-8 인코딩을 설정하시오.
# 2. 실행하면 줄 바꿈이 안 된다. 어떻게 처리할 것인가?

outfile = open(".\\file\\phones.txt", "a", encoding="UTF-8")

outfile.write("최무선 010-1111-2222\n" )
outfile.write("정중부 010-2222-3333\n")

outfile.close()
