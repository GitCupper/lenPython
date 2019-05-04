def test(num):
    print("在函数内部[%d]，对应的内存地址是：%d" % (num, id(num)))
    num = 77
    num += 1


a = 10
print("a 变量保存数据的内存地址是：%d" % id(a))

test(a)

print("a=%d" % a)
