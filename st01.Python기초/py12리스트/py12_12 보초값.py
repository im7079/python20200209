# sum = 0
avr = 0
sungjuk = []
print("종료하려면 음수를 입력하시오")
while True: #무한루프
    x = input("성적을 입력하시오") #x값 입력
    #정수로 변환
    x = int(x)
    #입력 값이 음수 이면 반복문을 종료.
    if x < 0: #x가 음수이면.
        break #반복문 종료
    sungjuk.append(x) # sungjuk 배열에 x값 추가

    #합계를 구한다.
    #sum=sum + x

   #평균을 구한다.
avr = sum(sungjuk) / len(sungjuk) #sum()함수 이용 리스트의 합을 len()함수 리스트의 갯수로 나눠 평균 구하기
    #합계를 출력한다.

str = "성적의 평균은 %s 입니다." %avr
print(str)