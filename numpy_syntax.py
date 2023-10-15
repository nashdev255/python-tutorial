import numpy as np
import random

a = [2, 3, 3]
b = [4, 5, 2]

a = np.array(a)
b = np.array(b)

print(a)
print(b)
print(np.dot(a, b))

c = []
for i in range(10):
  c.append(random.randint(0, 10))

print(c)
