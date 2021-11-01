sum = 0
mul = 1

for i in range(1, 1000001):
    mul /= 2
    sum += mul * i
    if i % 100000 == 0:
        print(i, sum, mul)
