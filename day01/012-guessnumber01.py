res = 45

input_num = 0

while True:
    input_num = int(input("请输入一个数字（1-100）："))
    if input_num < 0 or input_num > 100:
        print("You have inputted a wrong number.")
        break
    elif input_num < res:
        print("Your number is too small!")
    elif input_num > res:
        print("Your number is too big!")
    else:
        print("You are right, it is %d!" % res)
        break
