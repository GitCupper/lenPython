try:
    num = int(input("请输入一个整数："))
except ValueError:
    print("请输入正确的整数！")
except (ZeroDivisionError, ValueError):
    # 针对元组中的内容，进行异常处理
    pass
except Exception as result:
    print("未知错误 %s" % result)
else:
    # 没有异常才会执行的代码
    pass
finally:
    # 无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行的代码")

print("-" * 50)
