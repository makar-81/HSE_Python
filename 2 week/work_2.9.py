k = int(input())
if 5 <= k < 21 or 5 <= k % 10 <= 9 or k % 10 == 0:
    kor = "korov"
elif k % 10 == 1:
    kor = "korova"
elif 2 <= k % 10 < 5:
    kor = "korovy"
else:
    kor = "korov"
print(str(k), kor)
