
# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 3명이상
# 3. 학생 성적 입력 받기. 몇번 입력받아야 하는가?
# 4. list에 입력 받은 학생 성적을 추가한다.
# 5. 3번 학생의 성적을 100점으로 바꾸시오.
# 6. list에서 마지막 학생 삭제.
# 7. list에서 0번 값을 출력하시오.
# 8. 평균을 구하고 출력.

avr = 0
sum = 0
sungjuk = []
y = 0
z = input("학생수를 입력하시오: ")
z = int(z)
while y < z:
    x = input("성적을 입력하시오: ")  # x값 입력
    # 정수로 변환
    x = int(x)
    y = y+1
    sungjuk.append(x)  # sungjuk 배열에 x값 추가
    # 합계를 구한다.
    sum = sum + x

   # 평균을 구한다.
avr = sum / len(sungjuk)  # sum()함수 이용 리스트의 합을 len()함수 리스트의 갯수로 나눠 평균 구하기
# 합계를 출력한다.
print("합계는: ", sum)
print("평균은: ", avr)
