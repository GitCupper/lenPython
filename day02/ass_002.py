names = ["Lenovo", "Apple", "Benq", "Canon", "Dell", "Benz", "JBL"]
cnames = ["长虹", "华为", "腾讯"]

names.extend(cnames)

try:
    print(names[3])
    print(names.index("Canon"))
    print(names)
except (IndexError) as error:
    print("程序出错了，索引值超范围：%s" % error)
except (ValueError) as error:
    print("程序出错了，值不在列表中！%s" % error)
