a = 6
b = 100

# 解法1： 使用其他变量
c = a
a = b
b = c

# 解法2： 不使用其他变量
a = a + b
b = a - b
a = a - b

# 解法3： Python专有的，使用元组
a, b = (b, a)

print(a)
print(b)
