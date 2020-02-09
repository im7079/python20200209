v1=input("첫번째 과목 점수를 입력하셍요:")
v2=input("두번째 과목 점수를 입력하셍요:")

v1=int(v1) # 문자열 v1을 정수로 변환, 형변환
v2=int(v2) # 문자열 v2을 정수로 변환, 형변환

sum=v1+v2 #sum변수에 총점을 넣는다.
avr=sum/2 # avr변수에 평균을 넣는다.

print("----------------------------") #모니터 출력 "-"
if avr>=95 : # 조건문 평균이 95보다 크거나 같으면
    print("very good") # very good 출력
else : #95미만이면 
    print("just good") #just good 출력
print("----------------------------") #모니터 출력 "-"
