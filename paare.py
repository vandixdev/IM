import math

x = []

for i in range(10):
    for j in range(10):
        if (i*i + j*j) % 10 in [0, 1, 4, 5, 6, 9]:
            x.append((i, j))

print(x) 