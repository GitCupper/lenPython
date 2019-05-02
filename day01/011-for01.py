for i in range(1, 51, 2):
    print("i=%d" % i)


weeks = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Wednesday", "Sunday")

for week in weeks:
    print(week)

for food in ("pate", "cheese", "rotten apples", "crackers", "whip cream", "tomato soup"):
    if food[0:6] == "rotten":
        continue
    print("Hey you can %s" % food)
