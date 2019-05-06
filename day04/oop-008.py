class Phone(object):

    def __init__(self, name):
        self.name = name

    def bell(self):
        print("%s在响铃" % self.name)


class Apple(Phone):
    def bell(self):
        print("%s在响铃，是苹果！" % self.name)


class Huawei(Phone):
    def bell(self):
        print("%s在响铃，是华为！" % self.name)


class Player(object):
    def __init__(self, name):
        self.name = name

    def calle(self, phone):
        phone.bell()

# 关于Python的多态

p1 = Huawei("余承东")
p2 = Apple("库克")
c1 = Player("共享科惠")
c1.calle(p2)