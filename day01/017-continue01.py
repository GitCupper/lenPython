
def include_num(num, t):
    flag = False
    ss = str(num)
    for i in ss:
        if i == str(t):
            flag = True
            break
        else:
            flag = False

    return flag

for i in range(1, 1000):

    if i % 9 == 0 or include_num(i, 9):
        continue
    print(i)

# print(include_num(82, 8))
