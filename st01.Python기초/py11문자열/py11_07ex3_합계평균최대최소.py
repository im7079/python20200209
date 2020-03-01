# 합계 평균 최대 최소

temp3 = "74 874 9883 73 9 73646 774"
array1 = temp3.strip().split(" ")
print(array1)  # ['74', '874', '9883', '73', '9', '73646', '774']
# b. 문자열을 정수 리스트로 만든다.
array2 = []
for n in array1:
    n = int(n)
    array2.append(n)

print(array2)  # [74, 874, 9883, 73, 9, 73646, 774]

# 합계구하기
print("합계:", sum(array2))

#평균구하기
def avr(array2):
	v = 0
	for i in array2:
		v = v + i
	return v / len(array2)

print("평균", avr(array2))

# 최대값구하기
print("최대값", max(array2))

# 최소값구하기
print("최소값", min(array2))

