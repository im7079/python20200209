def get_sum(x, y):
    sum=0
    for i in range(x, y+1, 1):
        sum = sum + i
    print("함수출력",sum)


    return sum

a=3
b=7

get_sum(a, b)

#변수의종류
#전역변수: a, b
#지역변수: sum, i, x, y
#매개변수:함수 ()안에 있는 변수 위 코드에서 x, y