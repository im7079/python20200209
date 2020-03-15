#1. 문자열 입력 받기
#2. 문자열을 split()해서 array 리스트를 만든다.
#3. 반복문을 사용하여 array 리스트를 loop를 돌면서 딕셔너리 table에서 찾는다.
#3.1 table 찾았다면 바꾼다. replace()
#4문자열 메서드 join()을 사용하여 출력한다.

# 1.
table = {
    "B4": "before",
    "TX": "thanks",
    "BBL": "Be Back Later",
    "BCNU": "Be Seeing You",
    "HAND": "Have A Nice Day"
}

str = input("문자열을 입력하시오:")

#2. 문자열 나누기
array = str.split(" ")
result = " "
#3. 반복문
# for i in range(0, len(array), 1):
#    print(array[i]) #TX , Mr. , Park

for i in array: #리스트 방번호 반복문 추천
#    print(i) #Tx, Mr, Park!

#3-1. table에서 찾는다.
#찾을 때는 get()메서드나 in 연산자를 사용한다.
#찾았다면 바꾼다.
# array[0] = TX  일때 table에서 찾으려면( get() or in )
# array[1] = Mr. 일때 table에서 찾으려면( get() or in )
# array[2] = Park! 일때 table에서 찾으려면( get() or in )
    value = table.get( i ) # KeyError
    if value == None:
        result = result + i + " "

    else:
        result = result + result + value + " " # value =  array.[i]
#4. 출력한다.
print(result)
