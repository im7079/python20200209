# 중첩 for문

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# for문 1개를 이용하여 출력
# print("-------------------------------")
# for i in range(1, 11, 1):
#    for j in range(0, 10, 1):
#        print("*", end=" ")
#    print()  # 줄바꿈
#
# print("-------------------------------")

# print("-------------------------------")
# for i in range(1, 12, 1):
#    for j in range(1, i, 1):
#        print("*", end=" ")
#    print()  # 줄바꿈
#
print("-------------------------------")
for y in range(1, 10, 1):
    for x in range(1, 10, 1):
        if x < y:
            print('*', end='')
    else:
        print(' ', end='')
    print()
print("-------------------------------")
