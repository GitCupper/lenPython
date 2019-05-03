tstr = "hello world"

# 1. 是否以指定的字符开头
print(tstr.startswith('h'))

# 2. 是否以指定的字符结束
print(tstr.endswith("ld"))

# 3. 查找指定字符串
print(tstr.find("llo"))
print(tstr.find("abc"))

# 4. 替换字符串
print(tstr.replace('l', 'z'))
print(tstr)