# 리스트의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle


############################
# 리스트 선언
# 리스트에는 함수 포함 모두 담을 수 있다.
#array = []
#array = list()
#array = [1, 1.1, "문자", True, [0,1], {"a":1, "1":"ba"}, None]

# 문자 H, e, l, l, o를 요소로 가지는 리스트
list1 = ["H", "e", "l", "l", "o"]
print(type(list1), list1)  # <class 'list'> ['H', 'e', 'l', 'l', 'o']
list4 = list("Hello")
print(type(list4), list4)  # <class 'list'> ['H', 'e', 'l', 'l', 'o']
# 문자열 Hello를 요소로 가지는 리스트
list2 = ["Hello"]
print(type(list2), list2)  # <class 'list'> ['Hello']
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
list3 = [0, 1, 2, 3, 4]
print(type(list3), list3)  # <class 'list'> [0, 1, 2, 3, 4]

list5 = list(range(0, 5, 1))
print(type(list5), list5) #<class 'list'> [0, 1, 2, 3, 4]

# 공백 리스트 생성
# 문자열을 리스트로 변환. 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
############################
############################
# 리스트 요소 출력
# 리스트의 시작은 0번부터다.
# 리스트 Read : [] 선택 연산자를 사용한다.
############################
array = [1, 1.1, "문자", True, [0,1], {"a":1, "1":"ba"}, None]
print( "array[0]", type(array[0]), array[0]) #array[0] <class 'int'> 1
print( "array[0]", type(array[4]), array[4]) #array[0] <class 'list'> [0, 1]
print( "array[0]", type(array[5]), array[5]) #array[0] <class 'dict'> {'a': 1, '1': 'ba'}
print( "array[0]", type(array[6]), array[6]) #array[0] <class 'NoneType'> None
############################
# 리스트 출력
print( "array", array)
############################

############################
# 리스트 슬라이싱
# 1. 선택 연산자 사용하는 방법
print("array[0]", array[0])
print("array[1:3]", array[1:3])
print("array[-1]", array[-1])
############################

############################
# 리스트 요소 대입
# 리스트의 0번 값을 문자열 "변경" 값으로 바꾸시오.
print( "array[0]", array[0]) #1
array[0] = "변경"
print( "array[0]", array[0]) #변경
############################
# 리스트 요소 추가 : C. create
# 추가: 리스트에 마지막에 넣는다.--> .append()메서드 사용 
# 삽입: 리스트의 중간에 넣는다.--> .insert()메서드 사용
array.append("추가")
print("array", array) # array ['변경', 1.1, '문자', True, [0, 1], {'a': 1, '1': 'ba'}, None, '추가']
array.insert(0, "삽입")
print("array", array) # array ['삽입', '변경', 1.1, '문자', True, [0, 1], {'a': 1, '1': 'ba'}, None, '추가']

############################
# 리스트 요서 삭제: D. deletef
# 메서드 방식 --> pop()메서드, 추천
# 연산자 방식 --> del 비추천
array.pop(0)
print("array", array) #['변경', 1.1, '문자', True, [0, 1], {'a': 1, '1': 'ba'}, None, '추가']
del array[0]
print("array", array) #[1.1, '문자', True, [0, 1], {'a': 1, '1': 'ba'}, None, '추가']
############################
# 리스트 열거
for i in array:
    print("리스트열거", i)
############################

############################
# 복잡한 리스트
# 1차원 리스트
# 2차원 리스트
# 3차원 리스트
############################


############################
# 리스트에 담을 수 있는 것은?==> 모든것을 담을수 있다.
# 리스트 선언==>[], list()
# 리스트 추가(C) ==>추가:append(), insert()
# 리스트 읽기(R) ==> [방번호]
# 리스트 수정(U) ==> [방번호] = 값
# 리스트 삭제(D) ==> pop()
# 리스트 정렬(S) ==> sorted()
# 리스트 찾기(S) ==> .find() + 반복문, .rfind() + 반복문
# 리스트 길이    ==> len()
# 리스트 츌력    ==>
# 리스트 열거    ==>
# 리스트에 저장된 함수 실행하기
############################

############################
# 문자열 vs 리스트
############################
