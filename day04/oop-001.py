class Cat:
    """这是一个猫类"""

    def __init__(self):
        print("这是一个初始化方法")

        # 定义属性名
        self.name = "咪咪"

    def eat(self):
        print("The cat %s is eating." % self.name)

    def drink(self):
        print("The cat is drinking.")


# 创建猫对象
tom = Cat()
# tom.name = "刘罗锅"
tom.eat()
tom.drink()

larry = Cat()
larry.name = "喜来乐"
larry.eat()
larry.drink()

print(tom)
print(larry)

addr = id(tom)
print("%x" % addr)
