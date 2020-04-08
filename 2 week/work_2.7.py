a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (c - a == 0 or a - c == 0) and (b - d) % 2 == 0:
    print("YES")
elif (a - c == 1 or c - a == 1) and (b - d == 1 or d - b == 1):
    print("YES")
elif (a - c) % 2 == 0 and (b - d) % 2 == 0:
    print("YES")
elif ((a - c) + (b - d)) % 2 == 0:
    print("YES")
else:
    print("NO")
