file_name = "./speak.txt"

# 打开文件
file = open(file_name)

while True:
    text = file.readline()
    if not text:
        break
    print(text)

# 关闭文件
file.close()
