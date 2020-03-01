
y = 0
temp3 = []
while y < 10:
    x = input("INPUT") #x값 입력
    #정수로 변환
    x = int(x)
    #입력 값이 음수 이면 반복문을 종료.
    y = y + 1
    temp3.append[x]
    break #반복문 종료

# a. 문자열 자르기 --> 리스트를 얻게 됨.
lst = y.split(" ")  

# b. 문자열을 정수 리스트로 만든다.
lst[0] = int(lst[0])
for i in range(0, len(lst), 1):
    lst[i] = int(lst[i])

# c. 정수리스트를 오름차순 정렬하시오
lst = sorted(lst)
print("리스트 정렬 후:", lst)

# d. 정수리스트에서 최대값을 찾는다.
lst1 = min(lst)
print("최소값", lst1)

lst2 = max(lst)
print("최대값", lst2) 
