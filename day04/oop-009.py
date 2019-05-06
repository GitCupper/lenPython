class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        # 让类属性的值加一
        Tool.count += 1

    # 类方法需要敷衍＠classmethod进行注解，并使用cls作为第一个参数
    @classmethod
    def show(cls):
        pass


# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("剪子")

print(Tool.count)