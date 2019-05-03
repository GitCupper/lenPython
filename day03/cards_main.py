while True:
    action_str = input("请选择想要执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1, 2, 3针对名片的操作
    if action_str in ["1", "2", "3"]:
        pass
    # 0 退出系统
    elif action_str == "0":
        print("欢迎使用《名片管理系统》，再见！")
        break
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择！")
