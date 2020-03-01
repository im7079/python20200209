def main():
    temp3 = "74 874 9883 73 9 73646 774"

# a. 문자열 자르기 --> 리스트를 얻게 됨.
    lst = temp3.split(" ")  # ["74", "874", "9883", "73", "9", "73646", "774"
    print(type(lst), lst)  # ['74', '874', '9883', '73', '9', '73646', '774']

    print(lst[0], type(lst[0]))  # 74, <class 'str'>
    print(lst[1], type(lst[1]))  # 874, <class 'str'>
    print(lst[2], type(lst[2]))  # 9883, <class 'str'>

# b. 문자열을 정수 리스트로 만든다.
    lst[0] = int(lst[0])
    print(lst[0], type(lst[0]))  # 74, <class 'int'>

    for i in range(0, len(lst), 1):
        lst[i] = int(lst[i])
    print(type(lst), lst)  # 정수리스트 [9, 73, 74, 774, 874, 9883, 73646]

# c. 정수리스트를 오름차순 정렬하시오
    lst = sorted(lst)
    print(lst)
# d. 정수리스트에서 최대값을 찾는다.
    lst[len(lst)-1]  # 마지막방에 있는 값. len(lst) -1
    print(lst)
    lst = max(lst)
    print(lst)  # 73746

if __name__ == "__main__" :
    main()
