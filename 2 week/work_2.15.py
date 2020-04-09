a, b, c = int(input()), int(input()), int(input())
count = 0
if a == b and b == a:
    count += 1
if a == c and c ==a:
    count += 1
if b == c and c == b:
    count += 1
print(count)
