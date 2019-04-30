# 从控制台中输入数据
price = float(input("输入商品单价(0.01~100.00)："))
amount = int(input("输入商品的数量(1~10)："))

total_price = price * amount

# 由于Python中没有switch/case语句，故可以使用字典类型来实现switch/case语句，示例如下：
switcher = {
    0: "零",
    1: "壹",
    2: "贰",
    3: "叁",
    4: "肆",
    5: "伍",
    6: "陆",
    7: "柒",
    8: "捌",
    9: "玖",
    10: "拾",
}

print("%s件商品的价格是：￥%.02f元" % (switcher[amount], total_price))
