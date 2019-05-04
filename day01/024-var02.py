num = 10


# 修改全局变量，需要使用global关键字
def modify01():
    global num
    num = 99
    print("modify01 => %d" % num)


def modify02():
    print("modify02 => %d" % num)


modify01()
modify02()