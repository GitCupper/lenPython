# 从控制台中输入数据
price = input("输入商品单价：")

# 输入的数据是字符串，需要进行类型转换
print("五件商品的价格是：%f" % (float(price) * 5))
print("十件商品的价格是：%f" % (float(price) * 10))
