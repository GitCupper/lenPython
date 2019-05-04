# 多值参数
# 参数名前增加一个"*"，可以接收元组
# 参数名前增加两个"*"，可以接收字典

# 一般在给多值参数命名时，习惯使用以下两个名字
# *args 存放 元组 参数
# **kwargs 存放 字典 参数


def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="于谦", sex=True, age=45)

print("=" * 50)

# 元组、字典的拆包
# 要拆包元组，在元组变量前增加一个"*"
# 要拆包字典，在字典变量前增加两个"*
gl_nums = (1,2,3,4,5,6,7)
gl_dict = {"name": "毛泽东", "age": 84, "sex": True}

demo(55, *gl_nums, **gl_dict)