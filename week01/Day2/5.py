import math
a = 2
x = 1
for i in range(2,11):
    x = x + (1/a**2)
    a += 1
print(math.sqrt(x * 6))
