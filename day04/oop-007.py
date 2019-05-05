class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


# python中的继承是在括号中加入父类
class Dog(Animal):
    def bark(self):
        print("汪汪")


# 继承的传递
class Hasky(Dog):
    def jump(self):
        print("跳一跳")

    # 对父类方法的覆盖
    def run(self):
        print("跑十米")
        # 使用super()调用被覆盖的父类的方法
        super().run()

    # 创建一个对象：


wc = Dog()
wc.run()
wc.bark()

hs = Hasky()
hs.eat()
hs.run()

