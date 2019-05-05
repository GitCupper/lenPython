class Gun:

    def __init__(self, model):
        # 1. 枪的型号
        self.model = model
        # 2. 子弹的数量
        self.bullet_count = 0
        # 私有属性需要在属性前增加两个下划线：“__”
        self.__factory = "北方工业公司"

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1. 判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..." % self.model)
            return
            # 2. 发射子弹， -1
        self.bullet_count -= 1

        # 3. 提示发射信息
        print("[%s] 突突突... [%d]" % (self.model, self.bullet_count))

    def showFactory(self):
        print("[%s]是由[%s]生产的。" % (self.model, self.__factory))

    # 私有方法同样的需要在前面加上两个下划线“__”
    def __autoload(self):
        print("这是一个私有方法！")


class Soldier:
    def __init__(self, name):
        # 1. 姓名
        self.name = name
        # 2. 枪
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None:
            print("[%s]还没有枪..." % self.name)
            return
        # 2. 高喊口号
        print("冲啊 …… [%s]" % self.name)
        # 3. 让枪装填子弹
        self.gun.add_bullet(50)
        # 4. 让枪发射子弹
        self.gun.shoot()


ak47 = Gun("AK-47")
# ak47.add_bullet(40)
# ak47.shoot()
ak47.showFactory()

# 创建许三多
xsd = Soldier("许三多")
xsd.gun = ak47
xsd.fire()
print(xsd.gun)
