minutes = int(input())
hours = int((minutes - 1440 * (minutes // 1440)) // 60)
mins = int((minutes - 1440 * (minutes // 1440)) % 60)
print(hours, mins)
