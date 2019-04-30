# 从控制台中输入数据
price = float(input("输入商品单价(0.01~100.00)："))
amount = int(input("输入商品的数量(1~10)："))

total_price = price * amount

total = ""

if amount == 1:
    total = "一"
elif amount == 2:
    total = "二"
elif amount == 3:
    total = "三"
elif amount == 4:
    total = "四"
elif amount == 5:
    total = "五"
elif amount == 6:
    total = "六"
elif amount == 7:
    total = "七"
elif amount == 8:
    total = "八"
elif amount == 9:
    total = "九"
elif amount == 10:
    total = "十"
else:
    total = "零"

print("%s件商品的价格是：%f" % (total, total_price))
