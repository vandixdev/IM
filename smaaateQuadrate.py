import math

x = []

for i in range(1, 100):
    for j in range(i, 100):
        ab = math.sqrt(i*i+j*j)
        ab -= int(ab)
        doppelt = False
        if ab < 0.000001:
            for t in x:
                if abs(i/t[0] - j/t[1]) < 0.001:
                    doppelt = True
                    break
            if not doppelt:
                x.append((i, j, math.sqrt(i*i+j*j)))
print(x)
