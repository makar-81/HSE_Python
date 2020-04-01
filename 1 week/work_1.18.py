N = int(input())
finalTime = N - 86400 * (N // 86400)
hour = finalTime // 3600
minute = (finalTime - 3600 * hour) // 60
sec = finalTime % 60
print(hour, ':', minute // 10, minute % 10, ':', sec // 10, sec % 10, sep='')
