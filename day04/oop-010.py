class Computer(object):

    # 核心数
    cores = 0

    def __init__(self, name):
        self.name = name
        pass

    @classmethod
    def calc(cls):
        print("使用%d个核心进行计算" % cls.cores)
    Computer.cores += 1

    @staticmethod
    def show():
        print("显示提示信息！")


dell = Computer("戴尔")

Computer.calc()