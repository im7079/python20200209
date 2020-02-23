i=1 #변수 초기값 설정
sum =0 #변수 초기값 설정
while i<=100: # 변수 i 100까지
    if i%3 == 0: # 3의 배수 구하기
        sum=sum+i #3의배수 의 합

    #i를 1씩 증가시키면서    
    i = i+1
    str = "%s 부터 %s 사이의 3의 배수의 합은 %s입니다."%(1, 100, sum)
print(str)

#for문 합계 구하기
#sum=0
#for x in range(1, 10, 1):
    #3의배수
#     if i%3 == 0 
#    sum = sum+i

#print(sum)