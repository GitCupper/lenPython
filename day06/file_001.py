file_name = "./speak.txt"

"""
r 以只读方式打开文件
w 以可写方式打开文件
a 以追加方式打开文件
r+ 以读写方式打开文件，文件的指针将会放在文件的开头，如果文件不存在，抛出异常
w+ 以读写方式打开文件，如果文件存在会被覆盖。如果不存在，则创建新文件
a+ 以读写方式打开文件。如果该文件已经存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入
"""
f = open(file_name)
content = f.read()
print(content)
print("-" * 100)
text = f.read()
print(text)
# 关闭文件
f.close()
