class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是：%s，体重是：%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("我正在吃东西！")
        self.weight += 0.8



xm = Person("李世明", 76.92)
xm.run()
print(xm)
xm.eat()
print(xm)
