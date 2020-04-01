H = int(input())
A = int(input())
B = int(input())
print((H // A) * (A // H) + ((H // A) ( * ((H - A) // (A - B)))) + 1)
