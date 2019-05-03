def is_include_num(num, t):
    """检测输入的数字'num'中，是否包含数字't'"""
    flag = False
    ss = str(num)
    for i in ss:
        if i == str(t):
            flag = True
            break
        else:
            flag = False

    return flag


def say_hello():
    """打招呼"""
    print("Hello ", end="")
    print("World!")


def sum_2_num(x, y):
    """实现2个数字的求合"""
    print("%d + %d = %d" % (x, y, x + y))
    return x + y


def parameter(a, b):
    a = 999
    b = 000
    print("zp1:", a, "|", "zp2:", b)


def print_line(c, n):
    """打印n个c字符的分隔线。

    :param c: 分隔线字符
    :param n: 分隔线长度
    """
    print(c * n)


def print_lines(c, n, m):
    i = 0
    while i < m:
        print_line(c, n)
        i += 1

size = 100
title = "软件工程师"