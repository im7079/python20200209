#교재 72p, 78p, 80p , 134p참고한다.
#도전. 사용자로부터 임의의 개수의 성적을 받아서 평균을 계산한 후에 출력하는 프로그램 을 작성하여 보자, 센티널로는 음수의 값을 사용하자.
# 무한 반복과 반복문(루프) 탈출을 결합한예제\

#무한 반복문은 조건식을 True 로 하면 된다.
#루프 탈출은 break 를 사용하면 된다.
sum = 0
count = 0 
평균값 = 0
print("종료하려면 음수를 입력하시오")
while True: #무한루프
    입력값 = input("성적을 입력하시오")
    #정수로 변환
    입력값 = int(입력값)
    #입력 값이 음수 이면 반복문을 종료.
    if 입력값<0:
        break #반복문 종료
    else:
        count = count + 1 #입력 횟수

    #합계를 구한다.
    sum=sum + 입력값

   #평균을 구한다.
평균값 = sum / count
    #합계를 출력한다.

str = "성적의 평균은 %s 입니다." %평균값
print(str)

