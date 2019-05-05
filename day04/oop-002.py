class Cat:
    """这是一个猫类"""

    def __init__(self, name="Tom", age=5):
        print("这是一个初始化方法")
        self.name = name
        self.age = age

    def __del__(self):
        print("I'm %s, I'm dying." % (self.name))

    def __str__(self):
        # 必须要返回一个字符串
        return "I'm %s, %d years old." % (self.name, self.age)

    def eat(self):
        print("The cat %s is eating." % self.name)

    def drink(self):
        print("The cat is drinking.")

    def howOld(self):
        print("The cat %s age is: %d" % (self.name, self.age))


# 创建猫对象
tom = Cat()
# tom.name = "刘罗锅"
tom.eat()
tom.drink()
tom.howOld()

larry = Cat()
larry.name = "喜来乐"
larry.eat()
larry.drink()

sasan = Cat("刘老根", 65)
sasan.eat()
sasan.drink()
sasan.howOld()

print(tom)
print(larry)
print(sasan)

addr = id(tom)
print("%x" % addr)
