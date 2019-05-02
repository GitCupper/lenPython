import random

num = 0

rant = {"one": 0, "two": 0, "three": 0, "four": 0, "five": 0, "six": 0, "seven": 0, "eight": 0, "nine": 0, "ten": 0}

for i in range(1, 19999999, 1):
    num = random.randint(1, 10)
    if num == 1:
        rant["one"] += 1
    elif num == 2:
        rant["two"] += 1
    elif num == 3:
        rant["three"] += 1
    elif num == 4:
        rant["four"] += 1
    elif num == 5:
        rant["five"] += 1
    elif num == 6:
        rant["six"] += 1
    elif num == 7:
        rant["seven"] += 1
    elif num == 8:
        rant["eight"] += 1
    elif num == 9:
        rant["nine"] += 1
    elif num == 10:
        rant["ten"] += 1

# print(rant)

# python字符串的左右空格补全：str.rjust(5)，str.ljust(5)

for r in rant:
    print("%s->%10d" % (r.ljust(6), rant[r]))
