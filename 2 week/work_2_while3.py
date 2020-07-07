X, Y = int(input()), int(input())
Day = 0
while X <= Y:
    X += X * 0.1
    Day += 1
print(Day + 1)
