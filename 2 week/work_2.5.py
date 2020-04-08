a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c - a == 1 and (b - d == 1 or b - d == 0 or d - b == 1):
    print("YES")
elif a - c == 1 and (b - d == 1 or b - d == 0 or d - b == 1):
    print("YES")
elif a - c == 0 and (b - d == 1 or b - d == 0 or d - b == 1):
    print("YES")
else:
    print("NO")
