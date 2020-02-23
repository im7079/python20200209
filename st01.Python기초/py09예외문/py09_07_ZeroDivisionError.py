n1= input("숫자1 입력:")
n2= input("숫자2 입력:")

try:
    n1= int(n1)
    n2= int(n2)

    res= n1 / n2
except ValueError as ex:
    print("ValueError", ex)
except ZeroDivisionError as ex:
    print("ZeroDivisionError", ex)