# 1. 파일 읽고 문자열에 텍스트 저장
str = """This was a great help. 
I applied this method to similiar problem 
and rather than concat a SELECT statement 
I created an event scheduled every couple 
hours to rebuild a view that pivots n amount 
of rows from one table into n columns on the other. 
It is a big help because before I was rebuilding 
the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not 
be an issue as the pivoted rows->columns 
represent types of training employees at a 
franchise have so the view will not ever break 
a few thousand rows."""

# 2. 줄바꿈(\n) 을 제거한다.
str. replace("\n", "")  # .replace("  "," ")
# 3. 딕셔너리 table을 만든다.
table = {}
# 4. 문자열을 split() 해서 array 리스트로 만든다.
array = str.split(" ")
# 5. 반복문을 사용하여, array 리스트를 루프 돌면서
for i in range(0, len(array), 1):
    # print(i) #This, was
    # 5-1. 리스트 요소에서 첫글자를 추출한다. 선택연산자[] 사용
    # array[0] = This ==>0번방의 첫글자(array[0][0]) == T
    # array[1]= was ==>1번방의 첫글자array[1][0] == w
    # array[2]= a ==>2번방의 첫글자array[2][0] == a
    # array[4]= great ==>3번방의 첫글자array[3][0] == g
    key = array[i][0]
# 5-2. 대, 소문자를 구분하지 않도록 소문자로 치환한다.
    key = key.upper()
# 5-3. 딕셔너리 table 에서 키값중에 val 있는지 찾는다.
    tmp = table.get(key)  # 새로운 변수에 테이블의 값중 val을 찾는다.
# 5-4. 찾았다면 table[val] = table[val] + "-"
    if tmp == None:  # 미존재한다면
        #table[key] = "-"
        table[key] = 1
#     아니면 table[val] = "-"
    else:  # 존재한다면
        #table[key] = table[key] + "-"
        table[key] = table[key] + 1

# 6. 찾기가 끝나면 table 출력한다. 키와 값의 쌍으로 딕셔너리 열거 item()
for item in table.items():
    #print("items >>> ", item[0], item[1])
    print(item[0], item[1], item[0] * item[1])  # item[0] 을 item[1]번 반복하시오
    # item = (T, 17) => TTTTTTTTTTTTTTTTT
