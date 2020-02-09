# py02_09ex1_Salary

# 변수 선언 : salary , deposit 정수 변수 선언
salary = 0 # 변수선언 salary
deposit = 0 # 변수선언 deposit

# 정수를 입력받고 salary 변수 에 저장하시오.
salary=input("월급을 입력하세요:") # 변수salary를 정수형으로 변환해서 키보드 입력을 받는다.

# 10년치 월급의 총합을 구하고 그 값을 deposit 에 저장.
print( type(salary))
deposit=int(salary)*10*12 #10년치 월급의 합을 deposit에 넣는다.

# 10년 동안의 저축액: ?????  원 형태로 출력하시오.
print("10년 동안의 저축액:", deposit,"원") # 모니터 출력 변수에 저장된 데이터 출력