N = int(input())
n = 2
minDiv = N
while n <= N:
    if N % n == 0 and n < minDiv:
        minDiv = n
    n += 1
print(minDiv)
