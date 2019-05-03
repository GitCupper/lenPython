weeks = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", 23)

infos = ("Sky Flakes", 33.45)

print("品名：《%s》; 价格：￥%.2f元" % infos)

print("Today is: %s" % weeks[4])
for w in weeks:
    print(w)

print("#" * 50)
str = "中国人民解放军"
l1 = list(str)
print(type(str))
for l in l1:
    print(l)

print(str[2:4])

nstr = "四"
print(nstr.isdecimal())
print(nstr.isdigit())
print(nstr.isnumeric())
print("\u00b2")