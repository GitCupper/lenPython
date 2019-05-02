# 检测输入的数字num中，是否包含数字t
def is_include_num(num, t):
    flag = False
    ss = str(num)
    for i in ss:
        if i == str(t):
            flag = True
            break
        else:
            flag = False

    return flag