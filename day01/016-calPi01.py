import random
import math
import time

darts = 2 ** 30
hist = 0
time.clock()
for i in range(1, darts):
    x, y = random.random(), random.random()
    dist = math.sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        hist = hist + 1
pi = 4 * (hist / darts)
print('PI is %s' % pi)
print('Elapsed time is %ss' % time.clock())
