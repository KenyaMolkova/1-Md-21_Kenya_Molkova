x = '385916'
listik = list(x)
part1 = listik[:(len(listik)) // 2]
part2 = listik[(len(listik)) // 2:]
sum1 = 0
sum2 = 0
for i in part1:
    sum1 = sum1 + int(i)
for i in part2:
    sum2 = sum2 + int(i)
print(sum1)
print(sum2)