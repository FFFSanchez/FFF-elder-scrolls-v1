import random
k = 0
s = 4
n = 10**6       # количество испытаний

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if (x**2 + y**2) < 1:
        k += 1

P = (k / n) * s

print(P)

#print(0.7982864145030253**2 + (-0.8887435072547305)**2)

print('big boobs')