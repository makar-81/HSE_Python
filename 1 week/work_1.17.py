v = int(input())
t = int(input())
s = v * t
s = s - ((s // 109) * 109)
print(s)
