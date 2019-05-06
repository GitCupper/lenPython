# 复制大文件
old_file = "./speak.txt"
new_file = "speak[复件].txt"

# 打开文件
file_read = open(old_file)
file_write = open(new_file, "w")

# 读写文件
while True:
    # 读取一行内容
    text = file_read.readline()

    # 判断是否读取内容
    if not text:
        break

    file_write.write(text)

# 关闭文件
file_read.close()
file_write.close()
