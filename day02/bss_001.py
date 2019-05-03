students = [
    {"name": "唐玄奘"},
    {"name": "孙悟空"},
    {"name": "猪悟能"},
    {"name": "沙悟净"},
]

find_name = "孙悟空4"

for stu_dict in students:
    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break
else:
    print("没有找到 %s" % find_name)