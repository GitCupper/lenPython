def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 通过元组，返回多个值，其中的括号可以省略
    return (temp, wetness)


# 元组
result = measure()
print(result)

# 需要单独的处理温度或者温度
print(result[0])
print(result[1])

# 如果函数返回的类型是元组，同时希望单独处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果

gtemp, gwetness = measure()

print("温度：", gtemp)
print("湿度：", gwetness)
